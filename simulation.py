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
        for i in range(0, 1000):
            p.stepSimulation()
            # c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robotId, jointName="Torso_FrontLeg",
                                        controlMode=p.POSITION_CONTROL, targetPosition=c.frontLegAngles[i], maxForce=30)
            pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robotId, jointName="Torso_BackLeg",
                                        controlMode=p.POSITION_CONTROL, targetPosition=c.backLegAngles[i], maxForce=30)
            time.sleep(c.t)
        p.disconnect()