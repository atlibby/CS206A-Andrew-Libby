import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName, values):
        self.linkName = linkName
        # self.values was previously numpy.zeroes(10000)
        # change back if need be
        self.values = values

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # print(self.values[t], t, self.linkName)
        # exit()
        # remove exit and place sum of all touch sensor values into one variable
        # use variable in Robot Get_Fitness() to compute numpy.mean of variable
        # look at module F sensors module for help
        with open("data/t_sensor_vals.npy", "wb") as ts:
            np.save(ts, np.array(self.values[t]))
        ts.close()
    def Save_Values(self):
        np.save("data/sensorValues" + self.linkName, self.values)
