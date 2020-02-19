# import some modules
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr
import matplotlib.colors
from tkinter import *
from matplotlib import animation
from tkinter import colorchooser
from numba import jit

def fractal(real_min, real_max, imaginary_min, imaginary_max, real_points, imaginary_points, max_iterations=200,
            max_infinity_number=4):
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
    plt.imshow(image, cmap=cmap, interpolation='none')
    plt.show()


def update_frames(index):
    if index > maxFrames - 1:
        index = 0
    frame = gif_frames[index]
    index += 1
    label.configure(image=frame)
    label.after(50, update_frames, index)


def choose_color1():
    a = colorchooser.askcolor()[1]
    global color1
    color1 = a
    color_button.config(background=color1)

    global cmap

    colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20),
                                                         cycle([color1, '#000000',
                                                                color2, ]))]
    cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                                 colorpoints, N=2048)


def choose_color2():
    a = colorchooser.askcolor()[1]
    global color2
    color2 = a
    color_button_two.config(background=color2)

    global cmap

    colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20),
                                                         cycle([color1, '#000000',
                                                                color2, ]))]
    cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                                 colorpoints, N=2048)


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
        PhotoImage(master=root, file=r'C:\Users\ukolo\PycharmProjects\fractlas\mygif.gif', format='gif -index %i' % (i)) for i in range(maxFrames)]

    global color_button
    color_button = Button(text='Выбор цвета 2', command=choose_color1, master=root, background=color1)
    color_button.place(x=300, y=350)

    global color_button_two
    color_button_two = Button(text='Выбор цвета 1', command=choose_color2, master=root, background=color2)
    color_button_two.place(x=200, y=350)

    image_button = Button(text='Получить картинку', command=get_picture, master=root)
    image_button.place(x=10, y=350)

    gif_button = Button(text='Получить новую гиф', command=get_gif, master=root)
    gif_button.place(x=10, y=320)

    label = Label(root, width=380, height=300)
    label.place(x=10, y=0)
    root.after(0, update_frames, 0)
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
color1 = '#309fcf'
color2 = '#cf30bc'

colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20),
                                                         cycle([color1, '#000000',
                                                                color2, ]))]
cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                                 colorpoints, N=2048)


figure = plt.figure(figsize=(10, 10))
maxFrames = 30
maxZoom = 300
images = []

tkinter_window()