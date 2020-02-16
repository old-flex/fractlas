# import some modules
import numpy as np
import matplotlib.pyplot as plt

realMin = -2.5
realMax = 1.5

imaginaryMin = -2
imaginaryMax = 2

realPoints = 200
imaginaryPoints = 200

max_iterations = 300

maxInfinityNumber = 10

image = np.zeros((realPoints, imaginaryPoints))

realPart, imaginaryPart = np.mgrid[realMin:realMax:(realPoints * 1j), imaginaryMin:imaginaryMax:(imaginaryPoints * 1j)]

complexNumber = realPart + 1j * imaginaryPart
newComplex = np.zeros_like(complexNumber)

for i in range(max_iterations):
    newComplex = newComplex ** 2 + complexNumber


