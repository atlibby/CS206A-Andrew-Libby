import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(0, c.STEPS):
            p.stepSimulation()
            time.sleep(c.t)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
        p.disconnect()
