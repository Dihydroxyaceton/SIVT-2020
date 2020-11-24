from tkinter import *
import random

seed = random.randint(0, 10000000)
# seed = [BLANK]

print(seed)
#random.seed(seed)

window=Tk()
size = 500
cvs=Canvas(window, bg="#ffffff", width=size, height=size)
cvs.pack()

randomcolor = "#"+str(random.randint(100000, 999999))	# creates random hex code (for now: omitting #000000-#099999 and #aaaaaa-#ffffff)

def draw_symmetric_lines(start_X, start_Y, end_X, end_Y, color):
	cvs.create_line(start_X, start_Y, end_X, end_Y, fill=color)


	cvs.create_line(size-start_X, start_Y, size-end_X, end_Y, fill=color)

	
	cvs.create_line(start_X, size-start_Y, end_X, size-end_Y, fill=color)

	
	cvs.create_line(size-start_X, size-start_Y, size-end_X, size-end_Y, fill=color)

	
	
for i in range(2):
	draw_symmetric_lines(random.randint(0,size),random.randint(0,size),random.randint(0,size),random.randint(0,size),randomcolor)
	
window.mainloop()
