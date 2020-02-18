def plus_zoom():
    global maxZoom
    maxZoom += 1
    zoom_label.config(text="Teкущий зум: {}".format(maxZoom))


def minus_zoom():
    global maxZoom
    maxZoom -= 1
    zoom_label.config(text="Teкущий зум: {}".format(maxZoom))


def plus_frame():
    global maxFrames
    maxFrames += 1
    frame_label.config(text="Teкущее количество кадров в гифке: {}".format(maxFrames))


# Zoom label and button
    global zoom_label
    zoom_label = Label(text='Teкущий зум: {}'.format(maxZoom), master=root)
    zoom_label.place(x=10, y=10)

    zoom_button_plus = Button(text='+', master=root, command=plus_zoom)
    zoom_button_plus.place(x=120, y=10)

    zoom_button_minus = Button(text='-', master=root, command=minus_zoom)
    zoom_button_minus.place(x=140, y=10)

    # Frame label and button
    global frame_label
    frame_label = Label(text='Teкущее количесво кадров в гифке: {}'.format(maxFrames), master=root)
    frame_label.place(x=10, y=55)

    zoom_button = Button(text='+', master=root, command=plus_frame)
    zoom_button.place(x=300, y=55)