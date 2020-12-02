from tkinter import *
import random

seed = random.randint(0, 10000000)
# seed = [BLANK]

print(seed)
random.seed(seed)

window=Tk()
size = 500
cvs=Canvas(window, bg="#ffffff", width=size, height=size)
cvs.pack()


randomcolor = "#"

list_of_hex_characters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
position_in_list = random.randint(0,15)

for i in range(6):
	hex_char = list_of_hex_characters[position_in_list]
	randomcolor+=hex_char
	position_in_list = random.randint(0,15)

print(randomcolor)


def draw_symmetric_lines(start_X, start_Y, end_X, end_Y, color, thickness):
	cvs.create_line(start_X, start_Y, end_X, end_Y, fill=color, width=thickness)
	cvs.create_line(size-start_X, start_Y, size-end_X, end_Y, fill=color, width=thickness)
	cvs.create_line(start_X, size-start_Y, end_X, size-end_Y, fill=color, width=thickness)
	cvs.create_line(size-start_X, size-start_Y, size-end_X, size-end_Y, fill=color, width=thickness)

for i in range(7):
	draw_symmetric_lines(random.randint(0,size),random.randint(0,size),random.randint(0,size),random.randint(0,size),randomcolor,45)
	
window.mainloop()
