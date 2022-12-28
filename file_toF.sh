#!/bin/sh
#source /home/sora-desktop/anaconda3/etc/profile.d/conda.sh
#conda activate opensfm0
DIR_PATH=' /home/yamakawaryuto/毛利研究室/semantic_segmentation_main/Image_registration/ヒヤリハット_SfM/pitchi_ikami/'
cd $DIR_PATH

for file in `\find . -maxdepth 1 -type f`;
do
  echo $file
  FILE_NAME=`echo $file | sed -e 's/[^0-9]//g'`
  mv $file $FILE_NAME.csv
  #cp $file /home/yamakawaryuto/dataset/smrc/`$file | sed -e 's/[^0-9]//g'`/ikami_output.csv
done

dir_path="/home/yamakawaryuto/dataset/smrc/*"
dirs=`find $dir_path -maxdepth 0 -type d`
for dir in $dirs;
do
    echo $dir
    cd $dir
    CURRENT=$(cd $(dirname $0);pwd)
    DIR_NAME=`echo "$CURRENT" | sed -e 's/.*\/\([^\/]*\)$/\1/'`
    echo $DIR_NAME
    #cd /home/sora-desktop/OpenSfM
    #mkdir output
    #mkdir output/plotimage
    #python /home/sora-desktop/Documents/estimate_trajectory/save_data.py
    #sleep 3s
    #cd $dir
    cp $DIR_PATH/$DIR_NAME.csv $dir/ikami_output.csv
done