import numpy as np
import matplotlib.pyplot

fitnessValsA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fitnessValsB = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    npyNum = str(i)
    matrixA = np.load("matrixA" + ".npy")
    matrixB = np.load("matrixB" + ".npy")
    fitnessValsA[i] = matrixA.max()
    fitnessValsB[i] = matrixB.max()

matplotlib.pyplot.scatter(trials, fitnessValsA, color="red", label="Four-Legged Robot")
matplotlib.pyplot.scatter(trials, fitnessValsB, color="blue", label="Two-Legged Robot")
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.title("Maximum Fitness")
matplotlib.pyplot.xlabel("Trial")
matplotlib.pyplot.ylabel("Fitness Value")

matplotlib.pyplot.show()

for i in range(0,10):
    npyNum = str(i)
    A = np.load("matrixA" + ".npy")
    B = np.load("matrixB" + ".npy")
    A = np.mean(A, axis=0)
    B = np.mean(B, axis=0)

    if i == 0:
        matplotlib.pyplot.plot(A, color = "red", label = "Four Legged Robot")
        matplotlib.pyplot.plot(B, color = "blue", label = "Two Legged Robot")

    else:
        matplotlib.pyplot.plot(A, color = "red")
        matplotlib.pyplot.plot(B, color = "blue")

matplotlib.pyplot.legend(loc="upper left")
matplotlib.pyplot.title("All Averages")
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness Value")
matplotlib.pyplot.show()

A1 = np.load("matrixA1.npy")
A2 = np.load("matrixA2.npy")
A3 = np.load("matrixA3.npy")
A4 = np.load("matrixA4.npy")
A5 = np.load("matrixA5.npy")
A6 = np.load("matrixA6.npy")
A7 = np.load("matrixA7.npy")
A8 = np.load("matrixA8.npy")
A9 = np.load("matrixA9.npy")
A10 = np.load("matrixA10.npy")

A1 = np.mean(A1, axis=0)
A2 = np.mean(A2, axis=0)
A3 = np.mean(A3, axis=0)
A4 = np.mean(A4, axis=0)
A5 = np.mean(A5, axis=0)
A6 = np.mean(A6, axis=0)
A7 = np.mean(A7, axis=0)
A8 = np.mean(A8, axis=0)
A9 = np.mean(A9, axis=0)
A10 = np.mean(A10, axis=0)

A = np.mean(np.array([A1, A2, A3, A4, A5, A6, A7, A8, A9, A10], dtype=object), axis=0)

B1 = np.load("matrixB1.npy")
B2 = np.load("matrixB2.npy")
B3 = np.load("matrixB3.npy")
B4 = np.load("matrixB4.npy")
B5 = np.load("matrixB5.npy")
B6 = np.load("matrixB6.npy")
B7 = np.load("matrixB7.npy")
B8 = np.load("matrixB8.npy")
B9 = np.load("matrixB9.npy")
B10 = np.load("matrixB10.npy")

B1 = np.mean(B1, axis=0)
B2 = np.mean(B2, axis=0)
B3 = np.mean(B3, axis=0)
B4 = np.mean(B4, axis=0)
B5 = np.mean(B5, axis=0)
B6 = np.mean(B6, axis=0)
B7 = np.mean(B7, axis=0)
B8 = np.mean(B8, axis=0)
B9 = np.mean(B9, axis=0)
B10 = np.mean(B10, axis=0)

B = np.mean(np.array([B1, B2, B3, B4, B5, B6, B7, B8, B9, B10], dtype=object), axis=0)

stDevA = np.std(A)
stDevB = np.std(B)

matplotlib.pyplot.plot(A+stDevA, color = "red", label = "Four Legged Robot +/- Standard Devs")
matplotlib.pyplot.plot(A, color = "black", label = "Four Legged Robot")
matplotlib.pyplot.plot(A-stDevA, color = "red")

matplotlib.pyplot.plot(B+stDevB, color = "yellow", label = "Two Legged Robot +/- Standard Devs")
matplotlib.pyplot.plot(B, color = "blue", label = "Two Legged Robot")
matplotlib.pyplot.plot(B-stDevB, color = "yellow")

matplotlib.pyplot.legend(loc="lower left")
matplotlib.pyplot.title("Average of all Trials")
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness Value")

matplotlib.pyplot.show()
