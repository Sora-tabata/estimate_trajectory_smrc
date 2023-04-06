import numpy as np
from PIL import Image
import cv2
import os
from scipy import stats
import matplotlib.pyplot as plt

class Findhood():
    def __init__(self):
        pass
    
    def find_hood(self):
        ORIGINAL_FILE_DIR = "images/"
        MASK_FILE_DIR = "pred_mask/"
        mask = np.array(Image.open(path))
        buil = np.ones_like(mask)
        buil[mask == 30] = 0
        return buil*255

    def calc_hood(self):
        files = os.listdir("pred_mask/")
        hood_index = []
        for val in files:
            path = "pred_mask/" + val
            mask = np.array(Image.open(path))
            buil = np.ones_like(mask)
            buil[mask == 30] = 0
            hood = np.asarray(buil*255)
            #print(np.min(np.where(hood.T[int(len(hood.T[0])/2)] == 0)))
            #print(len(np.array(np.where(hood.T[0] == 255)).T))
            #hood_index.append(np.min())
            #hood_index_ = []
            for i in range(int(len(hood[0])/3), int(len(hood[0])*2/3)):
                try:
                    hood_index.append(np.min(np.where(hood.T[i]==0)))
                except:
                    continue
                #hood_index.append(np.min(np.where(hood.T[0]==0)))
        #print(hood_index)
        #print(int(stats.mode(hood_index, axis=0).mode[0]))
        '''
            plt.rcParams['font.family'] = 'Times New Roman'
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            plt.rcParams['font.family'] = 'Times New Roman'
            ax.hist(hood_index, bins=30, color='green', rwidth=0.8)
            #ax.set_title('Distribution of trajectories searched for multiple points')
            ax.set_xlabel('Mode of hood index for each images', fontsize=10)
            ax.set_ylabel('The number of hood index',fontsize=10)
            fig.savefig('output/hood_hist.png')
            plt.savefig('output/hood_hist.png')
        '''
        #bottom = int(stats.mode(hood_index, axis=0).mode[0])
        bottom = np.min(hood_index)
        return bottom
#print(Findhood().calc_hood())


        
