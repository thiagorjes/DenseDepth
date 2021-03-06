import os
import glob
import argparse
import time
from PIL import Image
import numpy as np
import PIL
import cv2

# Kerasa / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from loss import depth_loss_function
from utils import predict, display_images, to_multichannel, scale_up
from matplotlib import pyplot as plt

# Argument Parser
parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='my_examples/*.jpg', type=str, help='Path to Video')
args = parser.parse_args()

video_name = args.input
cap = cv2.VideoCapture(video_name)
cap.set(cv2.CAP_PROP_FPS, int(5))
fps=int(cap.get(cv2.CAP_PROP_FPS))
# out_video_name = 'output.avi'
# out = cv2.VideoWriter(out_video_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (1280, 480))



# Custom object needed for inference and training
start = time.time()
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': depth_loss_function}

print('Loading model...')

# Load model into GPU / CPU
model = load_model(args.model, custom_objects=custom_objects, compile=False)

print('\nModel loaded ({0}).'.format(args.model))


def get_img_arr(image):
    im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im = cv2.resize(im, (640, 480))
    x = np.clip(np.asarray(im, dtype=float) / 255, 0, 1)
    return x


def display_single_image(output, inputs=None, is_colormap=True):
    import matplotlib.pyplot as plt

    plasma = plt.get_cmap('plasma')

    imgs = []

    imgs.append(inputs)

    ##rescale output
    out_min = np.min(output)
    out_max = np.max(output)
    output = output - out_min
    outputs = output/out_max

    if is_colormap:
        rescaled = outputs[:, :, 0]
        pred_x = plasma(rescaled)[:, :, :3]
        imgs.append(pred_x)

    img_set = np.hstack(imgs)

    return img_set

os.system("mkdir image_results")

count = 0
ret = True

while ret:
    ret, image = cap.read()
    if ret is False:
        break
    img_arr = get_img_arr(image)
    output = scale_up(2, predict(model, img_arr, batch_size=1))
    pred = output.reshape(output.shape[1], output.shape[2], 1)
    img_set = display_single_image(pred, img_arr)
    img_out = img_set*255
    filename = 'img_' + str(count).zfill(4) + '.png'
    cv2.imwrite(os.path.join('image_results', filename),cv2.cvtColor(img_out.astype('float32'),cv2.COLOR_RGB2BGR))
    count += 1

os.system("ffmpeg -i image_results/img_%04d.png -c:v libx264 -pix_fmt yuv444p image_results/out.mp4 && mplayer image_results/out.mp4")
