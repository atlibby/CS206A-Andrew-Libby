import numpy
import matplotlib.pyplot
import matplotlib.pylab as plt

backLegSensorValues  = numpy.load('data/backLegSensorValues.npy')

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

targetAngleMotorValues = numpy.load('data/targetAngleData.npy')

#matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')

#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=2.0)

plt.plot(targetAngleMotorValues,numpy.sin(targetAngleMotorValues),label='Angle Data')

plt.legend()

plt.show()
