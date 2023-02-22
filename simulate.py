import random as r
import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import constants as c
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print ("Start: %s" % time.ctime())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
for i in range(0, 1000):
	p.stepSimulation()
	c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg",
	controlMode=p.POSITION_CONTROL, targetPosition=c.frontLegAngles[i], maxForce=30)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg",
	controlMode=p.POSITION_CONTROL, targetPosition=c.backLegAngles[i], maxForce=30)
	time.sleep(c.t)
with open('data/backLegSensorValues.npy', 'wb') as bl:
	numpy.save(bl,numpy.array(c.backLegSensorValues))
with open('data/frontLegSensorValues.npy', 'wb') as fl:
	numpy.save(fl,numpy.array(c.frontLegSensorValues))
with open('data/backLegAngleData.npy', 'wb') as tabl:
	numpy.save(tabl, numpy.array(c.backLegAngles))
with open('data/frontLegAngleData.npy', 'wb') as tafl:
	numpy.save(tafl, numpy.array(c.frontLegAngles))
print(c.frontLegSensorValues)
print(c.backLegSensorValues)
p.disconnect()
print ("End: %s" % time.ctime())
