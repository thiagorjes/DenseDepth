#!/bin/bash

CUDA_10_INSTALL=$1

# precisa do pip/python para funcionar - é python3
if  [ "$CUDA_10_INSTALL" == 1  ]; then
    echo "installing cuda 10 (depends)..."
    sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
    sudo apt-get update
    sudo apt-get install cuda-10-0

    sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.0_amd64.deb
fi;

echo "preparing virtual environment - python"
pip3 install virtualenv

echo "make venv"
virtualenv venv

echo "activating venv"
source venv/bin/activate

echo "installing pip dependencies on venv..."
pip3 install pathlib 
pip3 install keras==2.2.4 
pip3 install tensorflow-gpu==1.13.1 
pip3 install pillow 
pip3 install matplotlib 
pip3 install scikit-{learn,image} 
pip3 install opencv-python==4.2.0.32
pip3 install pydot 
pip3 install GraphViz
pip3 install h5py==2.10.0 --ignore-installed

deactivate

