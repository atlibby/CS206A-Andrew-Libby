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
for i in range(0, 1000):
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	print(backLegTouch)
	time.sleep(t)
p.disconnect()
print ("End: %s" % time.ctime())
