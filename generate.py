import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")

	width = 1

	length = 1

	height = 1

	x = 3

	y = 0.5

	z = -1

	pyrosim.Send_Cube(name="Box", pos=[z,x,y], size=[length,width,height])

	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	width = 1
	length = 1
	height = 1
	x = 0
	y = 0.5
	z = 0
	pyrosim.Send_Cube(name="Torso", pos=[z,x,y], size=[length,width,height])
	pyrosim.End()


Create_World()
Create_Robot()

