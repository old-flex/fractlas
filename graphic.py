# import some modules
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors
from tkinter import *
from matplotlib import animation
from tkinter import colorchooser


def fractal(real_min, real_max, imaginary_min, imaginary_max, real_points, imaginary_points, max_iterations=200,
            max_infinity_number=10):
    image = np.zeros((realPoints, imaginaryPoints))
    real_part, imaginary_part = np.mgrid[real_min:real_max:(real_points * 1j),
                                imaginary_min:imaginary_max:(imaginary_points * 1j)]

    complex_number = real_part + 1j * imaginary_part
    new_complex = np.zeros_like(complex_number)

    for i in range(max_iterations):
        new_complex = new_complex ** 2 + complex_number

        mask = (np.abs(new_complex) > max_infinity_number) & (image == 0)

        image[mask] = i

        new_complex[mask] = np.nan
    return -image.T


def init():
    return plt.gca()


def animation(i):
    if i > maxFrames // 2:
        plt.imshow(images[maxFrames // 2 - i], cmap='flag')
        print(i)
        return
    real_center = -0.793191078177363
    imaginary_center = 0.16093721735804

    zoom = (i / maxFrames * 2) ** 3 * maxZoom + 1
    scale = 1 / zoom
    new_real_min = (realMin - real_center) * scale + real_center
    new_imaginary_min = (imaginaryMin - imaginary_center) * scale + imaginary_center
    new_real_max = (realMax - real_center) * scale + real_center
    new_imaginary_max = (imaginaryMax - imaginary_center) * scale + imaginary_center

    image = fractal(new_real_min, new_real_max, new_imaginary_min, new_imaginary_max, realPoints, imaginaryPoints)
    plt.imshow(image, cmap='flag')
    images.append(image)
    print(i)
    return plt.gca()


def get_gif():
    anim = matplotlib.animation.FuncAnimation(figure, animation, init_func=init, frames=maxFrames, interval=50)
    anim.save('myGif.gif', writer=writer)


def get_picture():
    image = fractal(realMin, realMax, imaginaryMin, imaginaryMax, realPoints, imaginaryPoints, max_iterations,
                    maxInfinityNumber)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='flag', interpolation='none')
    plt.show()


def update_frames(index):
    if index > maxFrames - 1:
        index = 0
    frame = gif_frames[index]
    index += 1
    label.configure(image=frame)
    label.after(10, update_frames, index)


def choose_color():
    a = colorchooser.askcolor()
    print(a[1])

def tkinter_window():
    global label
    global gif_frames

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    width = width // 2 - 200
    height = height // 2 - 200

    root.geometry('400x400+{}+{}'.format(width, height))
    root.title('Редактор скринсейвера')

    gif_frames = [
        PhotoImage(master=root, file=r'C:\Users\ukolo\PycharmProjects\fractlas\mygif.gif', format='gif -index %i' % (i))
        for i in range(maxFrames)]

    color_button = Button(text='Выбор цвета', command=choose_color, master=root)
    color_button.place(x=300, y=350)
    # label = Label(root)
    # label.pack()
    #root.after(0, update_frames, 0)
    root.mainloop()


# Writer settings
writer = matplotlib.animation.ImageMagickWriter(fps=5, metadata=dict(artist='Me'), bitrate=1800)

# Settings for image
realMin = -2.5
realMax = 1.5
imaginaryMin = -2
imaginaryMax = 2
realPoints = 1000
imaginaryPoints = 1000
max_iterations = 200
maxInfinityNumber = 10

# Animation settings
figure = plt.figure(figsize=(10, 10))
maxFrames = 20
maxZoom = 10
images = []

tkinter_window()
