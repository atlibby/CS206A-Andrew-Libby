import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
t = 1/60
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print ("Start: %s" % time.ctime())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
for i in range(0, 100):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(t)
with open('data/backLegSensorValues.npy', 'wb') as bl:
	numpy.save(bl,numpy.array(backLegSensorValues))
with open('data/frontLegSensorValues.npy', 'wb') as fl:
	numpy.save(fl,numpy.array(frontLegSensorValues))
print(frontLegSensorvalues)
print(backLegSensorValues)
p.disconnect()
print ("End: %s" % time.ctime())
