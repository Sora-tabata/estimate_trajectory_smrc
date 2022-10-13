import numpy as np
import glob

class Init():
    def __init__(self):
        self.N0 = np.loadtxt(glob.glob('estimated_*')[0], encoding="shift-jis", delimiter=',', skiprows=1, usecols=[2, 6, 7, 8])
        self.M0 = np.loadtxt(glob.glob('ID*')[0], encoding="shift-jis", delimiter=',', skiprows=2, usecols=[8, 9, 10, 13])
        self.gps_t = np.loadtxt(glob.glob('ID*')[0], encoding="shift-jis", delimiter=',', skiprows=2, usecols=[30, 31])
        self.L0 = np.loadtxt('KeyFrameTrajectory.txt', delimiter=' ')
        self.json_file0 = open('reconstruction.json', 'r')
        self.n_frame = len(glob.glob("images/*.jpg"))
        self.len_groundtruth = len(np.loadtxt(glob.glob('ID*')[0], encoding="shift-jis", delimiter=',', skiprows=2, usecols=[16])) #ここを変更
        self.time_groundtruth = np.arange(self.len_groundtruth)*(1/100) #ここを変更
        self.Nx  = np.arange(self.n_frame)*(1/14)
        self.day = np.loadtxt(glob.glob('ID*')[0], encoding="shift-jis", dtype="unicode", delimiter=',', skiprows=2, usecols=[27])[0].replace('/', '-')
        self.time = np.loadtxt(glob.glob('ID*')[0], encoding="shift-jis", dtype="unicode", delimiter=',', skiprows=2, usecols=[16, 17, 18, 19])
        self.droid = np.vstack([np.load('tstamps.npy').T, np.load('poses.npy').T]).T