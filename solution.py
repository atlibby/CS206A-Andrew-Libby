import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        # if need be, replace 2 with c.numMotorNeurons below
        self.weights = self.weights * 2 - 1
        self.fitness = 0

    def Start_Simulation(self, directOrGUI, legs, letterID):
        self.Create_World()
        if (legs == 4):
            self.Create_Body()
            self.Create_Brain(self.myID)
        if (legs == 2):
            self.Create_Body2()
            self.Create_Brain2(self.myID)
        string = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + letterID
        os.system(string)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body_A" + str(self.myID) + ".urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1],
                          size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0],
                          size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                           child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0],
                          size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso",
                           child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0],
                          size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso",
                           child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0],
                          size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg",
                           child="LowerFrontLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg",
                           child="LowerBackLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg",
                           child="LowerLeftLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg",
                           child="LowerRightLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain(self, myID):
        pyrosim.Start_NeuralNetwork("brain_A" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="LowerRightLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="RightLeg_LowerRightLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=
                self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Create_Body2(self):
        pyrosim.Start_URDF("body_B" + str(self.myID) + ".urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1],
                          size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0],
                          size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                           child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0],
                          size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg",
                           child="LowerFrontLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg",
                           child="LowerBackLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain2(self, myID):
        pyrosim.Start_NeuralNetwork("brain_B" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="BackLeg_LowerBackLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=
                self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):

        randomColumn = random.randint(0, c.numSensorNeurons - 1)
        randomRow = random.randint(0, c.numMotorNeurons - 1)
        # if need be, replace 2 with c.numMotorNeurons below
        self.weights[randomColumn][randomRow] = random.random() * 2 - 1

    def Set_ID(self, myID):
        self.myID = myID