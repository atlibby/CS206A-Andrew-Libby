import random as r
import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
t = 1/60
backLegAmplitude = numpy.pi/6.0
backLegFrequency = 4
backLegPhaseOffset = 0
frontLegAmplitude = numpy.pi/4.0
frontLegFrequency = 4
frontLegPhaseOffset = numpy.pi/4.0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print ("Start: %s" % time.ctime())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
backLegAngles=numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
backLegAngles= backLegAmplitude * numpy.sin(backLegFrequency * backLegAngles + 
backLegPhaseOffset)
frontLegSensorValues = numpy.zeros(1000)
frontLegAngles=numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
frontLegAngles = frontLegAmplitude * numpy.sin(frontLegFrequency * frontLegAngles + 
frontLegPhaseOffset)
for i in range(0, 1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", 
	controlMode=p.POSITION_CONTROL, targetPosition=frontLegAngles[i], maxForce=30)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", 
	controlMode=p.POSITION_CONTROL, targetPosition=backLegAngles[i], maxForce=30)
	time.sleep(t)
with open('data/backLegSensorValues.npy', 'wb') as bl:
	numpy.save(bl,numpy.array(backLegSensorValues))
with open('data/frontLegSensorValues.npy', 'wb') as fl:
	numpy.save(fl,numpy.array(frontLegSensorValues))
with open('data/backLegAngleData.npy', 'wb') as tabl:
	numpy.save(tabl, numpy.array(backLegAngles))
with open('data/frontLegAngleData.npy', 'wb') as tafl:
	numpy.save(tafl, numpy.array(frontLegAngles))
print(frontLegSensorvalues)
print(backLegSensorValues)
p.disconnect()
print ("End: %s" % time.ctime())
