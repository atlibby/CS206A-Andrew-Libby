from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np


class PARALLEL_HILL_CLIMBER:
    def __init__(self, legs):
        os.system("rm brain_*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.legs = legs
        self.fitnessMatrix = np.zeros(shape=(c.populationSize, c.N_GENS))
        for parentNumber in range(c.populationSize):
            self.parents[parentNumber] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Spawn(self):
        self.children = {}

        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            # previously was >
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
                # self.children[key] = self.parents[key]

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.Fitness_Data(currentGeneration)

    def Fitness_Data(self, currentGeneration):
        population = 0
        for key in self.parents:
            fitVal = self.parents[key]
            self.fitnessMatrix[population][currentGeneration] = fitVal.fitness
            population += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.N_GENS):
            self.Evolve_For_One_Generation(currentGeneration)

    def Print(self):
        print()
        for key in self.parents:
            print("Parent:", self.parents[key].fitness, "Child:", self.children[key].fitness)
        print()

    def Evaluate(self, solutions):
        if self.legs == 4:
            letterID = "A"
            for solution in solutions:
                solutions[solution].Start_Simulation("DIRECT", self.legs, letterID)
        elif self.legs == 2:
            letterID = "B"
            for solution in solutions:
                solutions[solution].Start_Simulation("DIRECT", self.legs, letterID)

        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Show_Best(self):
        best_fit = self.parents[0]
        for parent in self.parents:
            if best_fit.fitness < self.parents[parent].fitness:
                #self.parents[parent] = best_fit
                best_fit = self.parents[parent]
        if self.legs == 4:
            letterID = "A"
            best_fit.Start_Simulation("GUI", self.legs, letterID)
        elif self.legs == 2:
            letterID = "B"
            best_fit.Start_Simulation("GUI", self.legs, letterID)
        file = open("data/fitVals.txt", "a")
        file.write(str(best_fit.fitness))
        file.close()
        if (self.legs == 2):
            test = "A"
        elif (self.legs == 4):
            test = "B"
        np.savetxt("matrix" + test + ".csv", self.fitnessMatrix, delimiter=", ")
        np.save("matrix" + test + ".npy", self.fitnessMatrix)
