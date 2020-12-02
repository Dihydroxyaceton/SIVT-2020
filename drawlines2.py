from tkinter import *
import random

'''default values:'''
seed=0
randomcolor = "#000000"
listOfUsedSeeds = []

'''customisable values:'''
canvasWidth=500
canvasHeight=300
lineThickness=5

"""
flowchart:
0.1) seed entered
1) button pressed
1.1) if no seed entered, will generate a random seed
2) random color generated
3) line drawn & ready for next button press
"""

def confirm():
	seed=seedEnterBox.get()
	if seed=="":
		seed = random.randint(0, 10000000)
	random.seed(seed)
	print("seed: "+str(seed))
	listOfUsedSeeds.append(seed)
	createRandomcolor()
	
def createRandomcolor():
	randomcolor = "#"
	listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	positionInList = random.randint(0,15)
	for i in range(6):
		hex_char = listOfHexCharacters[positionInList]
		randomcolor+=hex_char
		positionInList = random.randint(0,15)
	startDrawing(0, random.randint(0,canvasHeight), 10, random.randint(0,canvasHeight), randomcolor, lineThickness)
	
def startDrawing(start_X, start_Y, end_X, end_Y, color, thickness):
	for i in range(100):
		cvs.create_line(start_X, start_Y, end_X, end_Y, fill=color, width=thickness)
		start_X+=(canvasWidth/100)
		start_Y+=random.randint(-2, 2)
		end_X+=(canvasWidth/100)
		end_Y+=random.randint(-2, 2)

def undoLastMove():
	cvs.delete("all")
	if len(listOfUsedSeeds)!=0:
		listOfUsedSeeds.pop(-1)
		print("undo")
		for seedInList in listOfUsedSeeds:
			seed=seedInList
			random.seed(seed)
			createRandomcolor()
	else:
		print("cannot undo: canvas is already clear")
	
def resetCanvas():
	cvs.delete("all")
	print("reset")
	listOfUsedSeeds.clear()
	
tkWindow=Tk()
cvs=Canvas(tkWindow, bg="#ffffff", width=canvasWidth, height=canvasHeight)
cvs.pack()
seedEnterBox=Entry(tkWindow) # seed input
seedEnterBox.pack()
seedEnterButton=Button(tkWindow,text="GENERATE A LINE using SEED (leave empty for a random seed)",command=confirm,height=2,width=60) # button to confirm manual seed entry
seedEnterButton.pack()
undoButton=Button(tkWindow,text="UNDO",command=undoLastMove,height=2,width=60) # button to undo last move
undoButton.pack()
clearButton=Button(tkWindow,text="RESET (cannot be undone)",command=resetCanvas,height=2,width=60) # button to clear the canvas
clearButton.pack()

tkWindow.mainloop()
