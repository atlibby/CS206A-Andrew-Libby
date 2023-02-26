import numpy
t = 1/60
STEPS = 10000
AMPLITUDE = numpy.pi/6.0
FREQUENCY = 2
PHASE_OFFSET = 0
frontLegAmplitude = numpy.pi/4.0
frontLegFrequency = 4
frontLegPhaseOffset = numpy.pi/4.0

backLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
backLegAngles = AMPLITUDE * numpy.sin(FREQUENCY  * backLegAngles +
PHASE_OFFSET)

frontLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
frontLegAngles = frontLegAmplitude * numpy.sin(frontLegFrequency * frontLegAngles + 
frontLegPhaseOffset)
