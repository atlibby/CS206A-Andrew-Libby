import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time as t
import os

iteration = 0
while iteration <= 10:
    # segment = 1
    legs = 4
    print("Simulating 4-legged jumping")
    c.numSensorNeurons = 5
    c.numMotorNeurons = 8
    phcA = PARALLEL_HILL_CLIMBER(legs)
    phcA.Evolve()
    phcA.Show_Best()

    t.sleep(1)

    legs = 2
    print("Simulating 2-legged jumping")
    c.numSensorNeurons = 3
    c.numMotorNeurons = 2
    phcB = PARALLEL_HILL_CLIMBER(legs)
    phcB.Evolve()
    phcB.Show_Best()

    t.sleep(1)

    iteration += 1

os.system("python3 plotFitnessValues.py")
