import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

width = 1

length = 1

height = 1

x = 0

y = 0.5

z = 0

pyrosim.Send_Cube(name="Box", pos=[z,x,y], size=[length,width,height])

pyrosim.End()


