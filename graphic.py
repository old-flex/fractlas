# import some modules
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors
import tkinter


def fractal(realMin, realMax, imaginaryMin, imaginaryMax, realPoints, imaginaryPoints, max_iterations,
            maxInfinityNumber):
    image = np.zeros((realPoints, imaginaryPoints))
    realPart, imaginaryPart = np.mgrid[realMin:realMax:(realPoints * 1j),
                              imaginaryMin:imaginaryMax:(imaginaryPoints * 1j)]

    complexNumber = realPart + 1j * imaginaryPart
    newComplex = np.zeros_like(complexNumber)

    for i in range(max_iterations):
        newComplex = newComplex ** 2 + complexNumber

        mask = (np.abs(newComplex) > maxInfinityNumber) & (image == 0)

        image[mask] = i

        newComplex[mask] = np.nan
    return -image.T


# Settings for image
realMin = -2.5
realMax = 1.5
imaginaryMin = -2
imaginaryMax = 2
realPoints = 200
imaginaryPoints = 200
max_iterations = 200
maxInfinityNumber = 10

# ImShow
plt.figure(figsize=(10, 10))

image = fractal(realMin, realMax, imaginaryMin, imaginaryMax, realPoints, imaginaryPoints, max_iterations,
                maxInfinityNumber)
plt.xticks([])
plt.yticks([])
# plt.imshow(image, cmap='flag', interpolation='none')
# plt.show()

# Window
root = tkinter.Tk()
root.geometry('600x400+200+100')
c = tkinter.Canvas(root)
c.pack()
c.create_image(image=image)
root.mainloop()
