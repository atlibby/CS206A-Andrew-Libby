import pybullet as p
import time
t = 1/60
physicsClient = p.connect(p.GUI)
print ("Start: %s" % time.ctime())
p.loadSDF("box.sdf")
for i in range(0, 1000):
	p.stepSimulation()
	time.sleep(t)
p.disconnect()
print ("End: %s" % time.ctime())
