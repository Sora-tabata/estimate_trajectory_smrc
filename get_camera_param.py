import numpy as np
import sys
import os
import shutil
import pandas as pd
import glob

class GetCameraParam():
    def __init__(self):
        self.camera_type = pd.read_csv(glob.glob('ID*')[0]).iloc[0, 13]

    def getCamparam(self):

        #args = sys.argv
        #shutil.copy('../config.yaml', 'config.yaml')
        #camera_param = pd.ExcelFile('camera_param.xlsx')
        #sheet_df = camera_param.parse('videoID_carame_parameters')
        #camera_id = args[1]
        #sheet_df = pd.read_excel('../camera_param.xlsx', sheet_name = 'videoID_carame_parameters')
        #print(args[1])
        #camera_type = sheet_df.at[sheet_df['VideoID'].tolist().index(int(camera_id)), 'CameraType']
        print(self.camera_type)
        if (self.camera_type == 'DRU-5010'):
            shutil.copy('../../camera_params/denso.json', 'camera_models_overrides.json')
            shutil.copy('../../camera_params/denso.txt', 'calib.txt')
            shutil.copy('../../camera_params/denso.yaml', 'calib.yaml')
        elif (self.camera_type == '堀場試作品'):
            shutil.copy('../../camera_params/horiba.json', 'camera_models_overrides.json')
            shutil.copy('../../camera_params/horiba.txt', 'calib.txt')
            shutil.copy('../../camera_params/horiba.yaml', 'calib.yaml')
        elif (self.camera_type == 'DR-3031'):
            shutil.copy('../../camera_params/3031.json', 'camera_models_overrides.json')
            shutil.copy('../../camera_params/3031.txt', 'calib.txt')
            shutil.copy('../../camera_params/3031.yaml', 'calib.yaml')
        elif (self.camera_type == 'DR-6200'):
            shutil.copy('../../camera_params/6200.json', 'camera_models_overrides.json')
            shutil.copy('../../camera_params/6200.txt', 'calib.txt')
            shutil.copy('../../camera_params/6200.yaml', 'calib.yaml')
        elif (self.camera_type == 'DR-9100'):
            shutil.copy('../../camera_params/9100.json', 'camera_models_overrides.json')
            shutil.copy('../../camera_params/9100.txt', 'calib.txt')
            shutil.copy('../../camera_params/9100.yaml', 'calib.yaml')
        else:
            print('NO CAMERA TYPE, PLEASE CHECK YOUR ID, OR REGISTER NEW ID INTO THE EXCEL FILE')

GetCameraParam().getCamparam()