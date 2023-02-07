import numpy
import matplotlib.pyplot

backLegSensorValues  = numpy.load('data/backLegSensorValues.npy')

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')

matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=2.0)

matplotlib.pyplot.legend()

matplotlib.pyplot.show()
