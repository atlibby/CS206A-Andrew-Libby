import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

width = 1

length = 1

height = 1

x = 0

y = 0.5

z = 0

for g in range(5):
	width = 1
	length = 1
	height = 1
	for h in range(5):
		width = 1
		length = 1
		height = 1
		for i in range(10):
			pyrosim.Send_Cube(name="Box", pos=[z+g,x+h,y+i], 
size=[length,width,height])
			width *= .9
			length *= .9
			height *= .9

pyrosim.End()


