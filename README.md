This repository can integrate multiple SLAM(Simultaneous Localization and Mapping) and SfM(Structure from Motion) systems using nonholonomic constraints and finaly can convert estimated trajectory to latitude and longitude coordinates using road networks.
The target of dataset is assumed to be Hiyarihat-data in SMRC. 



## Table of Contents
- [Preparation](#preparation)
  * [Prepare Docker](#prepare-docker)
  * [Prepare Conda](#prepare-conda)
- [Installation](#installation)
  * [Clone repo](#clone-repo)
  * [Python requirements](#python-requirements)
  * [Download weights](#download-weights)
- [Running Localization Systems](#running-localization-systems)
  * [ORB_SLAM3](#orb_slam3)
  * [OpenSfM](#opensfm)
  * [DROID-SLAM](#droid-slam)
- [Integrate Localization systems](#integrate-localization-systems)
  * [Running](#running)
  * [Optional](#(optional))
- [Convert latitude and longitude coodinate](#convert-to-latitude-and-longitude-coodinate)
  * [Multi-Point-Search(Optional)](#multi-point-search-optional)
- [Links](#links)

## Preparation
* _This repository is only tested with ubuntu 18.04 LTS, Docker 23.0.1, and CUDA 11.3._
### Prepare Docker
You can install docker on Ubuntu by seeing [this](https://docs.docker.com/desktop/install/ubuntu/). <br>
After installation, check your docker by following command.
```bash
docker --version
```
### Prepare Conda
You can install anaconda on Ubuntu by seeing [this](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html).<br>
After installation, exit your current terminal and reopen.


## Installation
### Clone repo
Firstly, clone this repo with recursive flag.
```bash
git clone --recursive https://github.com/smart-mobility-research-center/estimate_trajectory_smrc
```
### Python requirements
Install most requirement of your conda environment by following command:
```bash
pip install -r requirements.txt
```
But you need another environment when running semantic-segmentation and velocity-estimation. Please see [SemanticSegmentation](https://github.com/smart-mobility-research-center/SemanticSegmentation) and [velocity_estimation](https://github.com/smart-mobility-research-center/velocity_estimation) repo in SMRC org.
### Download weights
#### ORB_SLAM3
1．Download the model from google drive：[ORBvoc.txt](https://drive.google.com/file/d/1ZDA2VEHCiJv1I91gNXKajZn0JOO9Kiyl/view?usp=share_link)<br>
2．Put ORBvoc.txt under `Localizations/ORB_SLAM3/Vocabulary/` directory. 
#### DROID-SLAM
1．Download the model from google drive：[droid.pth](https://drive.google.com/file/d/1PpqVt1H4maBa_GbPJp4NwxRsd9jk-elh/view?usp=sharing)<br>
2．Put droid.pth under `Localizations/DROID-SLAM/` directory. 
#### Semantic-Segmentation
1．Download the model from google drive：[hrnetv2_w48_imagenet_pretrained.pth](https://drive.google.com/file/d/1PDoAvVaLqhCMYFKeBAvZ1rkQsx4O4HDB/view?usp=share_link) and [BestCheckpoints.pth](https://drive.google.com/file/d/1gK3RZHLKiWHfUZhV9GIpETOf_7rsQNP4/view?usp=share_link).<br>
2．Put `hrnetv2_w48_imagenet_pretrained.pth` under `semantic-segmentation/seg_weights/` , and `BestCheckpoints.pth` under `semantic-segmentation/weights/` directory.
### Prepare working space(dataset)
Please prepare your own Hiyarihat-data as following data structure.
``` - OpenCv
{YOUR_HIYARI_DATASET_NAME}
 - images
   -ID****
   -ID*****
   …

 - csv
   -ID****
   -ID*****
   …
```
To running this repo, change dataset structure as following.
``` - OpenCv
estimate_trajectory_smrc
  - data_ws
    - ID****
      -images
      -pred_mask
      …

    - ID*****
      -images
      -pred_mask
      …
```
So, please run following command so that create new dataset directory.<br>
Write path to {YOUR_HIYARI_DATASET_NAME} to {PATH_TO_YOUR_HIYARI_DATASET_NAME} in absolute paths.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/build_ws.sh {PATH_TO_YOUR_HIYARI_DATASET_NAME}
```
Then, data_ws directory is created.<br>
Next, run semantic-segmentation and get `pred_mask` dir for each ID.</br> 
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_segmentation.sh
```
Finally, please run following command to prepare files for running localizaion sysmtems.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_trim.sh
```
#### Add drive-recorder devices(optional)
To add drive-recorder devices in addition to DRU-5010, please edit `get_camera_param.py` and include param files to `camera_params` directory. <br>
* _The name of drive-recorder is refered the particular cell in ID****.csv. Please see `get_camera_param.py.`_
## Running Localization systems
### ORB_SLAM3
Create container：
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source Localizations/ORB_SLAM3/build_container_cuda.sh
```
Usage：
```bash
docker exec -it orbslam3 bash
root@YOUR_PC_NAME:$ cd /estimate_trajectory_smrc
root@YOUR_PC_NAME:$ source batch_files/batch_orbslam.sh
```
### OpenSfM
Create container：
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source Localizations/OpenSfM/build_container.sh
```
Usage：
```bash
docker exec -it opensfm bash
root@YOUR_PC_NAME:/$ cd /estimate_trajectory_smrc
root@YOUR_PC_NAME:/$ source batch_files/batch_opensfm.sh
```
### DROID-SLAM
Create container：
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source Localizations/DROID-SLAM/build_container.sh
```
Usage：
```bash
docker exec -it droidslam bash
(droidenv)root@YOUR_PC_NAME:/$ cd /estimate_trajectory_smrc
(droidenv)root@YOUR_PC_NAME:/$ source batch_files/batch_droidslam.sh
```

## Integrate Localization systems
### Running
You can run this script (integration of localization systems) by following commands.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/integrate_system.sh
```
And then, create `result_dir` directory.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_output.sh
```
To get the output results,  please see under the `result_dir` directory.
### (Optional)
You can speed up your processing when the data is so large by using parallel processing (multi-process).
Please see [this](https://phoenixnap.com/kb/bash-wait-command).
## Convert to latitude and longitude coodinate
Firstly, please extract Road-Network from (OpenStreetMap) by the following command.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_roadnetwork.sh
```
Then, `extracted_roads.csv` is created for each ID folders in `data_ws`.<br>
Next, convert to latitude and longitude coodinate by following commands.<br>
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_latlon.sh {TRAJECTORY_TO_USE}
```
Please input one of the following commands in the `{TRAJECTORY_TO_USE}`, 
``` - OpenCv
orb
sfm
droid
optimized
```
To get the output results,  please see under the `result_dir` directory.

### Multi-Point-Search (Optional)
Accuracy may be improved by using multi-point search.<br>
Please run the following command before running `batch_latlon.sh`.
```bash
cd /{PATH_TO_YOUR_REPO}/estimate_trajectory_smrc
source batch_files/batch_explore.sh
```
And then, run `batch_latlon.sh` again.
## Links

* [SAKURA-project](https://wwww.sakura-prj.go.jp)
* [Semantic-Segmenation](https://github.com/NVIDIA/semantic-segmentation)
* [ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)
* [OpenSfM](https://github.com/mapillary/OpenSfM)
* [DROID-SLAM](https://github.com/princeton-vl/DROID-SLAM)
* [OpenStreetMap](https://www.openstreetmap.org)