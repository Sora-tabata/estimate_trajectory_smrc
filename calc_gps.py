from calc_traj import CalcTraj
import gps2coord, coord2gps
import numpy as np
import glob
from scipy import integrate, signal, interpolate
from init import Init
from calc_traj import CalcTraj

class CalcGPS():
    def __init__(self):
        self.N0 = Init().N0
        self.M0 = Init().M0
        self.gps_t = Init().gps_t
        self.L0 = Init().L0
        self.json_file0 = Init().json_file0
        self.groundtruth = CalcTraj().calcGroundTruth(self.N0, self.M0)
        self.orbslam = CalcTraj().calcOrbslam(self.groundtruth, self.L0)
        self.opensfm = CalcTraj().calcOpensfm(self.groundtruth, self.json_file0)

    def calcCoord(self):
        coord_t = []
        for i in range(len(self.gps_t)):
            coord = gps2coord.calc_xy(self.gps_t[i][0], self.gps_t[i][1], self.gps_t[0][0], self.gps_t[0][1])
            coord_t.append([coord[0], coord[1]])
        return coord_t
    
    @staticmethod
    def rot2coord(self, est):
        est_ = [np.array(est[0]), np.array(est[1])]
        x_ = np.vstack([est_[1], est_[0]]).T
        y_ = np.vstack([CalcGPS().groundtruth[1][8::7], CalcGPS().groundtruth[0][8::7]]).T
        U, S, V = np.linalg.svd(x_.T @ y_)
        #U, S, V = np.linalg.svd(np.diff(x_, axis=0).T @ np.diff(y_, axis=0))
        R = V.T @ U.T
        coord_est = [-(R @ x_.T)[0], (R @ x_.T)[1]]
        return coord_est
    
    def coord2gps_est(self, est):
        gps_est = []
        coord_est_ = CalcGPS().rot2coord(self, est)
        for i in range(len(coord_est_[0])):
            gps = coord2gps.calc_lat_lon(np.array(coord_est_[0])[i], np.array(coord_est_[1])[i], self.gps_t[0][0], self.gps_t[0][1])
            gps_est.append([gps[0], gps[1]])
        return gps_est