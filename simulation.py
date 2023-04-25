import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time
import numpy as np


class SIMULATION:
    def __init__(self, directOrGUI, solutionID, letterID):
        self.directOrGUI = directOrGUI
        self.letterID = letterID
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD(solutionID)
        if letterID == "A":
            self.robot = ROBOT(solutionID, letterID)
        elif letterID == "B":
            self.robot = ROBOT(solutionID, letterID)
        self.sensorArray = []

    def Run(self):
        for i in range(0, c.STEPS):
            p.stepSimulation()
            time.sleep(c.t)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def Get_Fitness(self):
        sensorDataArray = []
        for sensorKey in self.robot.sensors:
            sensorClassInstance = self.robot.sensors[sensorKey]
            sensorDataArray.append(sensorClassInstance.values)
        sensorMatrix = np.array(sensorDataArray)
        airTime = 0
        for array in sensorMatrix:
            for index in array:
                if index == -1:
                    airTime += 1
        sensorMean = airTime / sensorMatrix.size
        contigFile = open("data/sensorAvg.txt", "w")
        contigFile.write(str(sensorMean))
        contigFile.close()
        self.robot.Get_Fitness()
        return sensorMean


    def __del__(self):
        p.disconnect()
