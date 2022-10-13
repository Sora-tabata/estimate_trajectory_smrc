import folium
import numpy as np
from folium.plugins import TimestampedGeoJson
import glob
from calc_traj import CalcTraj
from calc_gps import CalcGPS
import gps2coord, coord2gps
from init import Init

class CreateStaticMap():
    def __init__(self):

        self.groundtruth = CalcTraj().calcGroundTruth(Init().N0, Init().M0)
        self.orbslam = CalcTraj().calcOrbslam(self.groundtruth, Init().L0)
        self.opensfm = CalcTraj().calcOpensfm(self.groundtruth, Init().json_file0)

        self.gps_t = Init().gps_t
        self.gps_slam = np.array(CalcGPS().coord2gps_est(self.orbslam))
        self.gps_sfm = np.array(CalcGPS().coord2gps_est(self.opensfm))

        self.gps_t = self.gps_t.tolist()
        self.gps_slam = self.gps_slam.tolist()
        self.gps_sfm = self.gps_sfm.tolist()

    def createTime(self):
        times = []
        output = []
        for i in range(len(Init().time)):
            times.append("T"+str(Init().time[i][3])+":"+str(Init().time[i][2])+":"+str(Init().time[i][1]))
            output.append(Init().day+times[i])
        return output
    
    def drawPolyLine(self):
        m = folium.Map(location=self.gps_t[0], zoom_start=20)

        folium.PolyLine(self.gps_t, color='black', weight=0.5).add_to(m)
        folium.PolyLine(self.gps_slam, color='green', weight=0.5).add_to(m)
        folium.PolyLine(self.gps_sfm, color='red', weight=0.5).add_to(m)
        m
        m.save('output/map.html')