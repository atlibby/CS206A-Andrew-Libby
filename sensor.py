import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName, values):
        self.linkName = linkName
        # self.values was previously numpy.zeros(10000)
        # change back if need be
        self.values = values

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values[t]

    def Save_Values(self):
        np.save("data/sensorValues" + self.linkName, self.values)
