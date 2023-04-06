import os
import glob
import numpy as np
import pandas as pd

class MakeTestList():
    def __init__(self):
        self.path = glob.glob('images/*.jpg')
        self.fps = pd.read_csv(glob.glob('ID*')[0]).iloc[0, 14]
        self.n_frame = len(glob.glob("images/*.jpg"))

    def print(self):
        print(self.path, "jpg")
    
    @staticmethod
    def makeData(self):
        data = []
        for f in self.path:
            data.append(os.path.split(f)[1])
            #print(os.path.split(f)[1])
        return sorted(data)

    def exportFile(self):
        with open('test_list.txt', 'w') as f:
            for i in MakeTestList.makeData(self):
                f.write("%s\n" % i)
    
    def exportTimes(self):
        times_list = []
        for i in range(self.n_frame):
            times_list.append(i/self.fps)
        np.savetxt('times.txt', times_list)

MakeTestList().exportTimes()