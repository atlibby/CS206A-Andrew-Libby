import pybullet_data
import pybullet as p
import time
t = 1/60
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print ("Start: %s" % time.ctime())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for i in range(0, 1000):
	p.stepSimulation()
	time.sleep(t)
p.disconnect()
print ("End: %s" % time.ctime())
