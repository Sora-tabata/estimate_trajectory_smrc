#!/bin/sh
#source /home/sora-desktop/anaconda3/etc/profile.d/conda.sh
#conda activate opensfm0



#cd /home/sora-desktop/ORB_SLAM3
dir_path="/home/sora-desktop/Documents/sample_data_2/*"
dirs=`find $dir_path -maxdepth 0 -type d`

for dir in $dirs:
do
    echo $dir
    cd $dir
    rm -rf image_0
    rm -rf reports
    rm -rf exif
    rm -rf masks
    rm -rf matches
    rm -rf pred_mask
    rm -rf undistorted
    rm -rf features
    #mkdir image_0
    #python /home/sora-desktop/createmap/trim.py
    
    #python /home/sora-desktop/createmap/create_mask.py 
    #rename 's/image_0/images/' $dir/image_0
    #cp /home/sora-desktop/dataset/times.txt $dir/times.txt
    #cp /home/sora-desktop/dataset/camera_models_overrides.json $dir/camera_models_overrides.json
    #cp /home/sora-desktop/dataset/config.yaml $dir/config.yaml
    #cp /home/sora-desktop/Documents/camera_models_overrides.json $dir/camera_models_overrides.json
    #cp /home/sora-desktop/Documents/rename.py $dir/masks/rename.py
    #cp /home/sora-desktop/Documents/rename.sh $dir/masks/rename.sh
    #cd $dir/masks
    #source ./rename.sh
    #rm rename.sh
    #rm rename.py
    #cd $dir
    #rm -rf undistorted
    #bin/opensfm_run_all $dir
    #./Examples/Monocular/mono_kitti Vocabulary/ORBvoc.txt Examples/Monocular/denso.yaml $dir
    #cp /home/sora-desktop/ORB_SLAM3/KeyFrameTrajectory.txt $dir/KeyFrameTrajectory.txt
done
