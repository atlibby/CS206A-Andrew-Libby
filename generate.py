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
	pyrosim.Send_Cube(name="Link0", pos=[z,x,y], size=[length,width,height])
	pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", 
position=[0,0,1])
	pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", 
position=[0,0,1])
	pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", 
position=[0,0.5,0.5])
	pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0], size=[length,width,height])
	pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", 
position=[0,1,0])
	pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0], size=[length,width,height])
	pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", 
position=[0,1,0])
	pyrosim.Send_Cube(name="Link5", pos=[0,-0.5,-1], size=[length,width,height])
	pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", 
position=[0,0,-1.5])
	pyrosim.Send_Cube(name="Link6", pos=[0,-0.5,-0.5], size=[length,width,height])
	pyrosim.End()

def Create_Bot():
	pyrosim.Start_URDF("body.urdf")
	width = 1
	length = 1
	height = 1
	pyrosim.Send_Cube(name="Torso", pos=[1.0,1.0,1.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", 
type="revolute", position=[1.5,0.5,1])
	pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0.5,-0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", 
type="revolute", position=[0.5,0.5,1])
	pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0.5,-0.5], 
size=[length,width,height])
	pyrosim.End()
	
Create_World()
Create_Bot()
