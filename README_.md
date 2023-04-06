### [Paper](https://arxiv.org/abs/2005.10821) | [YouTube](https://youtu.be/odAGA7pFBGA)  | [Cityscapes Score](https://www.cityscapes-dataset.com/method-details/?submissionID=7836) <br>

### [日本語はこちら](docs/ReadME_JP.md)

This repo contains inference implementation for paper [Hierarchical Multi-Scale Attention for Semantic Segmentation](https://arxiv.org/abs/2005.10821).<br>

This script can do image un-distortion (if there are camera intrinsic parameters), and then run segmentation for input images/directory.

## Table of Contents
- [Installation](#installation)
  * [Python requirements](#python-requirements)
  * [Install Apex](#install-apex)
    + [Linux](#linux)
    + [Windows](#windows)
- [Download pre-trained weights](#download-pre-trained-weights)
- [Configuration](#configuration)
- [Others](#others)


## Installation

* _The code is only tested with PyTorch 1.13.0 and Python 3.8_

### Python requirements
Python >= 3.8 is required to run this script. Other python packages are:
``` - OpenCv
 - Pytorch
 - Pyyaml
 - Numpy
 - Scikit-learn
 - Scikit-image
 - Tqdm
 - brotli
```
Install most above requirement by following command:
```bash
pip install -r requirements.txt
```

**Note:** If you want to install on **Windows**, install **Apex** before install PyTorch to avoid error. <br>
Install choose suitable <mark style="background-color: rgb(255, 255, 128)">PyTorch version (CUDA version is required)</mark> from [here](https://pytorch.org/get-started/locally/).<br>

### Install Apex

#### Linux
Run following command to install Apex or clone from [Apex repository](https://github.com/NVIDIA/apex)

```bash
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

#### Windows
First, install C++ development environment requirements via Visual Studio Build Tools.
* Download & open Visual Studio from [here](https://aka.ms/vs/17/release/vs_buildtools.exe)
* During installing screen, check :ballot_box_with_check: `Desktop development with C++`, then `install`. Default installation should be same as bellow:
![VS Environment](docs/VS_environment.png "Default installation")


Then, run following command to install Apex via built-in python only
```bash
cd apex
pip install -v --disable-pip-version-check --no-cache-dir ./
```

## Download pre-trained weights

* Download backbone weights **hrnetv2_w48_imagenet_pretrained.pth** from [google drive](https://drive.google.com/open?id=1fs-uLzXvmsISbS635eRZCc5uzQdBIZ_U) and put into `./weights` directory.
* Download other `Hiyarihat` data pre-trained weights and put into same directory. 
One way to get pre-trained weight is access to 452-Sever and get: `192.168.1.7/sharefolder/Lan/Segmentation_Semantic/2022_new_best_SMRC_trained.pth`


## Configuration
Before running this cript, modify (or create) `*.yaml` in `configs` directory. Most relevant parameters are:
 - `dataset`: Name of which datasets that used when trained your weight. (cityscapes, A2D2, SMRC, etc.)
 - `architect`: Network architecture. Currently, only trained with HRNet_Mscale.
 - `snapshot`: Name of pre-trained weight, that must be in weights folder.
 - `cam_param`: Camera Intrinsic parameter that used for un-distortion. `null` if you don't need image un-distortion.
 - `upscale_method`: Method used to up-scaling image after un-distort image. (bilinear, cubic)
- `batch_size_val`: Batch size when run inference. `batch_size_val=10` requires about 20Gb GPU memory.
- `eval_folder`: Path to image directory to run inference.
- `result_dir`: Path to save the result(s).

## Inference
Run bellow command to run inference with your modified configuration:

```bash
python inference.py --config ocrnet_hrnet_w48.yaml
```


## Others

* TRAINING & VALIDATION: This scrip is only focus on inference, so there is no code for training or validation. Training and validation scrip is available [here](https://github.com/NVIDIA/semantic-segmentation). But that scrip is only support Linux OS.
* Inference time: Raise `batch size` seem not fasten inference time, because most inference time is write output result. 