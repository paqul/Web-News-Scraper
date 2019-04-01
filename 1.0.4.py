from tkinter import *
import os


mainwindow = Tk()
mainwindow.title('Web-Scraper')

frame_root = Frame(mainwindow)
frame_root.grid(row=0, column=0, sticky=N)


#-------------------Frame 0 0 ---------------------------#
frame_0_0 = Frame(frame_root)
frame_opcje = LabelFrame(frame_0_0, text="Options", relief="groove", width=50, height=50)

# button_test = Button(frame_opcje, text="OPCJE 0 0", width=50, height=10)
# button_test.grid()

frame_opcje.grid()
frame_0_0.grid(row=0, column=0, columnspan=3)

#-------------------Frame 0 1 ---------------------------#
frame_0_1 = Frame(frame_root)
frame_search = LabelFrame(frame_0_1, text="Search", relief="groove")


entry_label = Label(frame_search, text="Search:")#, height=15, width=20)
entry_label.grid(row=0, column=3, columnspan=1, sticky=E)

entry_text = Entry(frame_search, width=25)
entry_text.grid(row=0, column=4, columnspan=2, sticky=W,  pady=60)

frame_search.grid(row=0, column=3, columnspan=3, padx=5, pady=5)
frame_0_1.grid(row=0, column=3, columnspan=3)#, padx=10, pady=10)

#-------------------Frame 2 0 ---------------------------#
frame_2_0 = Frame(frame_root)


tvn_logo_img = PhotoImage(file="tvn.png")
first_logo = Label(frame_2_0, image=tvn_logo_img)
first_logo.image = tvn_logo_img
first_logo.grid()

frame_2_0.grid(row=2, column=0)

#-------------------Frame 2 1 ---------------------------#
frame_2_1 = Frame(frame_root)

tvp_logo_img = PhotoImage(file="tvp.png")
second_logo = Label(frame_2_1, image=tvp_logo_img)
second_logo.image = tvp_logo_img
second_logo.grid()

frame_2_1.grid(row=2, column=1)

#-------------------Frame 2 2 ---------------------------#
frame_2_2 = Frame(frame_root)

polsat_logo_img = PhotoImage(file="polsat.png")
third_logo = Label(frame_2_2, image=polsat_logo_img)
third_logo.image = polsat_logo_img
third_logo.grid()

frame_2_2.grid(row=2, column=2)

#-------------------Frame 2 3 ---------------------------#
frame_2_3 = Frame(frame_root)

wp_logo_img = PhotoImage(file="wp.png")
fourth_logo = Label(frame_2_3, image=wp_logo_img)
fourth_logo.image = wp_logo_img
fourth_logo.grid()

frame_2_3.grid(row=2, column=3)

#-------------------Frame 2 4 ---------------------------#
frame_2_4 = Frame(frame_root)

onet_logo_img = PhotoImage(file="onet.png")
fiveth_logo = Label(frame_2_4, image=onet_logo_img)
fiveth_logo.image = onet_logo_img
fiveth_logo.grid()

frame_2_4.grid(row=2, column=4)

#-------------------Frame 2 5 ---------------------------#
frame_2_5 = Frame(frame_root)

interia_logo_img = PhotoImage(file="interia.png")
sixth_logo = Label(frame_2_5, image=interia_logo_img)
sixth_logo.image = interia_logo_img
sixth_logo.grid()

frame_2_5.grid(row=2, column=5)

print('MAIN')

#-------------------Frame horizontal ---------------------------#
frame_1_0 = Frame(frame_root)

empty_space_horizontal_1 = Label(frame_1_0, bg="red", width=100)
empty_space_horizontal_1.grid()

frame_1_0.grid(row=1, column=0, columnspan=15)

frame_3_0 = Frame(frame_root)

empty_space_horizontal_3 = Label(frame_3_0, bg="orange", width=100)
empty_space_horizontal_3.grid()

frame_3_0.grid(row=3, column=0, columnspan=15)

#-------------------Frame Vertical ---------------------------#
frame_0_7 = Frame(frame_root)

empty_space_vertical = Label(frame_0_7, bg="blue", width=3, height=30)
empty_space_vertical.grid()

frame_0_7.grid(row=0, column=7, rowspan=7)

mainwindow.mainloop()
