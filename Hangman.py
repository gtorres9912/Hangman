from graphics import *
import random

#Window Settings
win = GraphWin("Hang Man",650,650)
win.setCoords(0.0, 0.0, 10.0, 10.0)
win.setBackground("white")

#Horizontal Line
Line(Point(1.5,7),Point(5,7)).draw(win)
Line(Point(0,0.1),Point(3,0.1)).draw(win)
#Vertical Line
Line(Point(5,7),Point(5,5)).draw(win)
Line(Point(1.5,0.1),Point(1.5,7)).draw(win)

#Entry box
inputText = Entry(Point(7,7),5)
inputText.draw(win)
inputText.setTextColor("white")

#Random word generator
listOfWords = ["ford", "word", "water", "lake", "pokemon", "computer", "python"]
index = random.randint(0,6)
print(listOfWords[index])
randomWord = listOfWords[index]

#Number of spaces for word
if (len(randomWord) == 8):
    lineLength = 9
elif (len(randomWord) == 4):
    lineLength = 5
elif (len(randomWord) == 7):
    lineLength = 8
elif (len(randomWord) == 5):
    lineLength = 6
elif (len(randomWord) == 6):
    lineLength = 7
Line(Point(1.5,8.5),Point(lineLength,8.5)).draw(win)
i = 0
x = 2
while(i < len(randomWord)):
    Spaces = Line(Point(x,8.5),Point(x + 0.5, 8.5)).draw(win)
    Spaces.setOutline("white")
    i += 1
    x += 1
    
#Checking letters entered
numberOfAttempts = 0
while (numberOfAttempts < 7):
    win.getMouse()
    usersGuess = inputText.getText()
    for letter in randomWord:
        if (letter == usersGuess):
            txt = Text(Point(1.7,8.7), letter)
            txt.draw(win)
            
if (numberofAttempts == 6):
    youLost = Text(Point(5,9.5),"You Lost")
    youLost.setSize(20)
    youLost.setFace("courier")
    youLost.draw(win)
    
