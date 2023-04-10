from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy as np


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body" + self.solutionID + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + self.solutionID + ".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, np.zeros(c.STEPS))

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle * c.motorJointRange)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        sensorArray = np.load("data/t_sensor_vals.npy")
        sensorAvg = np.mean(sensorArray)
        print("Touch sensor average: " + str(sensorAvg))
        tempFitness = open("tmp" + self.solutionID + ".txt", "w")
        tempFitness.write(str(xPosition))
        tempFitness.close()
        os.system("mv tmp" + self.solutionID + ".txt" " fitness" + self.solutionID + ".txt")

