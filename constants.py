import numpy
t = 1/60
backLegAmplitude = numpy.pi/6.0
backLegFrequency = 4
backLegPhaseOffset = 0
frontLegAmplitude = numpy.pi/4.0
frontLegFrequency = 4
frontLegPhaseOffset = numpy.pi/4.0
backLegSensorValues = numpy.zeros(1000)
backLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
backLegAngles = backLegAmplitude * numpy.sin(backLegFrequency * backLegAngles + 
backLegPhaseOffset)
frontLegSensorValues = numpy.zeros(1000)
frontLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
frontLegAngles = frontLegAmplitude * numpy.sin(frontLegFrequency * frontLegAngles + 
frontLegPhaseOffset)
