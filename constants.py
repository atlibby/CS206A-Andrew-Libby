import numpy
t = 1/1000
populationSize = 1
motorJointRange = 0.5
STEPS = 1000
N_GENS = 1
AMPLITUDE = numpy.pi/6.0
FREQUENCY = 2
PHASE_OFFSET = 0
frontLegAmplitude = numpy.pi/4.0
frontLegFrequency = 4
frontLegPhaseOffset = numpy.pi/4.0
numSensorNeurons = 5
numMotorNeurons = 8
backLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
backLegAngles = AMPLITUDE * numpy.sin(FREQUENCY  * backLegAngles +
PHASE_OFFSET)

frontLegAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 1000)
frontLegAngles = frontLegAmplitude * numpy.sin(frontLegFrequency * frontLegAngles + 
frontLegPhaseOffset)
