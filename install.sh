#!/bin/bash

# Check for conda
if command -v conda &> /dev/null; then
    conda_version=$(conda --version)
    echo "Conda is installed. Version: $conda_version"
else
    echo "Install conda first."
fi

# Create environment
conda create --name nerfstudio -y python=3.8
conda activate nerfstudio
python -m pip install --upgrade pip

# PyTorch & cuda
pip uninstall torch torchvision functorch tinycudann
pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch

#Install nerfstudio
pip install nerfstudio
ns-install-cli