from tkinter import *


mainwindow = Tk()
mainwindow.title('Web-Scraper')

frame_root = Frame(mainwindow).grid(row=0, column=0, sticky=N)


#-------------------Frame 0 0 ---------------------------#
frame_0_0 = Frame(frame_root)

button_test = Button(frame_0_0, text="opt 0 0")
button_test.grid()

frame_0_0.grid(row=0, column=0, columnspan=3)

#-------------------Frame 0 1 ---------------------------#
frame_0_1 = Frame(frame_root)

button_test = Button(frame_0_1, text="searcher 0 1")
button_test.grid()

frame_0_1.grid(row=0, column=3, columnspan=3)

#-------------------Frame 2 0 ---------------------------#
frame_2_0 = Frame(frame_root)

button_test = Button(frame_2_0, text="logo 2 0")
button_test.grid()

frame_2_0.grid(row=2, column=0)


#-------------------Frame 2 1 ---------------------------#
frame_2_1 = Frame(frame_root)

button_test = Button(frame_2_1, text="logo 2 1")
button_test.grid()

frame_2_1.grid(row=2, column=1)

#-------------------Frame 2 2 ---------------------------#
frame_2_2 = Frame(frame_root)

button_test = Button(frame_2_2, text="logo 2 2")
button_test.grid()

frame_2_2.grid(row=2, column=2)

#-------------------Frame 2 3 ---------------------------#
frame_2_3 = Frame(frame_root)

button_test = Button(frame_2_3, text="logo 2 3")
button_test.grid()

frame_2_3.grid(row=2, column=3)

#-------------------Frame 2 4 ---------------------------#
frame_2_4 = Frame(frame_root)

button_test = Button(frame_2_4, text="logo 2 4")
button_test.grid()

frame_2_4.grid(row=2, column=4)

#-------------------Frame 2 5 ---------------------------#
frame_2_5 = Frame(frame_root)

button_test = Button(frame_2_5, text="logo 2 5")
button_test.grid()

frame_2_5.grid(row=2, column=5)

print('MAIN')

#-------------------Frame horizontal ---------------------------#
frame_1_0 = Frame(frame_root)

empty_space_horizontal = Label(frame_1_0, bg="red", width=100)
empty_space_horizontal.grid()

frame_1_0.grid(row=1, column=0, columnspan=15)

#-------------------Frame Vertical ---------------------------#
frame_0_7 = Frame(frame_root)

empty_space_vertical = Label(frame_0_7, bg="blue", width=3, height=10)
empty_space_vertical.grid()

frame_0_7.grid(row=0, column=7, rowspan=7)

mainwindow.mainloop()
