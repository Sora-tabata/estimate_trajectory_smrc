from view_coord import ViewCoord
from calc_traj import CalcTraj
from create_staticmap import CreateStaticMap
from create_dynamicmap import CreateDynamicMap
from init import Init

class Main():
    def __init__(self):
        self.N0 = Init().N0
        self.M0 = Init().M0
        self.gps_t = Init().gps_t
        self.L0 = Init().L0
        self.json_file0 = Init().json_file0
        self.droid = Init().droid
        self.groundtruth = CalcTraj().calcGroundTruth(self.N0, self.M0)
        self.orbslam = CalcTraj().calcOrbslam(self.groundtruth, self.L0)
        self.opensfm = CalcTraj().calcOpensfm(self.groundtruth, self.json_file0)
        self.doidslam = CalcTraj().calcDroidslam(self.groundtruth, self.droid)

if __name__ == '__main__':
    print("output")
    #CreateDynamicMap().drawMap()
    #CreateStaticMap().drawPolyLine()
    a = ViewCoord()
    a.showTrajectory(a.groundtruth, a.opensfm, a.orbslam, a.doidslam)
    
