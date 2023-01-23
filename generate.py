import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

width = 2

length = 1

height = 3

x = 0

y = 1.5

z = 0

pyrosim.Send_Cube(name="Box", pos=[z,x,y] , size=[length,width,height])

pyrosim.End()


