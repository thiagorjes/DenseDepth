import fill_depth_colorization as f
import matplotlib as plt

output=f.fill_depth_colorization("/media/thiago/Elements/TEMP/kitti/2011_09_26/2011_09_26_drive_0096_sync/image_03/data/0000000100.png","display /media/thiago/Elements/TEMP/thiago/train/2011_09_26_drive_0096_sync/proj_depth/groundtruth/image_03/0000000100.png")
plt.imshow(output)
plt.show()