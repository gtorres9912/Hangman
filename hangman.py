from graphics import *
import random

#Done by Miguel Lopez and Gustavo Torres
#To run this program you will need the graphic library
#To install the graphics library you need to type "pip install graphics.py" into the command prompt

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
#Button to click
guessButton = Rectangle(Point(8,7),Point(9.2,6))
guessButton.setFill("black")
guessButton.draw(win)
guessButtonLabel = Text(Point(17.2/2,13/2),'Click to Guess')
guessButtonLabel.setSize(8)
guessButtonLabel.setTextColor("white")
guessButtonLabel.draw(win)

#Random word generator
listOfWords = ["ford", "word", "water", "lake", "pokemon", "computer", "python", "sweater", "april", "avocado", "digimon", "photoshop", "eucalyptus", "soccer", "basketball", "java", "illustrate", "music"]
index = random.randint(0,17)
randomWord = listOfWords[index]
correctGuesses = 0
correctGuessesArray = []

#Put the random word into an array
randomWordArray = []
n = 0
while (n < len(randomWord)):
    randomWordArray.insert(n + 1, randomWord[n])
    n += 1

#Number of spaces for word
if (len(randomWord) == 4):
    lineLength = 4
elif (len(randomWord) == 5):
    lineLength = 5
elif (len(randomWord) == 6):
    lineLength = 6
elif (len(randomWord) == 7):
    lineLength = 7
elif (len(randomWord) == 8):
    lineLength = 8
elif (len(randomWord) == 9):
    lineLength = 9
elif (len(randomWord) == 10):
    lineLength = 10
Line(Point(0.5,8.5),Point(lineLength,8.5)).draw(win)
i = 0
x = 1
while(i < len(randomWord)):
    Spaces = Line(Point(x,8.5),Point(x + 0.5, 8.5)).draw(win)
    Spaces.setOutline("white")
    i += 1
    x += 1
    
#Checking letters entered
game = True
numberOfAttempts = 0
while (game):
    p = win.getMouse()
    if (p.getX() < 8 or p.getX() > 9.2 or p.getY() < 6 or p.getY() > 7):
        continue
    usersGuess = inputText.getText()
    if usersGuess in randomWord:
        bob = 0
        totalTimes = 0
        times = 0
        for letters in randomWord:
            if (letters == usersGuess):
                totalTimes += 1
        if usersGuess not in correctGuessesArray:
            temp = 1
            correctGuessesArray.insert(temp,usersGuess)
            temp += 1
            
            if(randomWord[bob] == usersGuess):
                txt = Text(Point(0.7 + bob,8.7), usersGuess)
                txt.draw(win)
                correctGuesses += 1
                times += 1
            else:
                while(randomWord[bob] != usersGuess):
                    bob +=1 
                    if(randomWord[bob] == usersGuess):
                        txt = Text(Point(0.7 + bob,8.7), usersGuess)
                        txt.draw(win)
                        correctGuesses += 1
                        times += 1
            while(totalTimes != times):
                bob += 1
                if(randomWord[bob] == usersGuess):
                    txt = Text(Point(0.7 + bob,8.7), usersGuess)
                    txt.draw(win)
                    correctGuesses += 1
                    times += 1
        if (correctGuesses == len(randomWord)):
            userWins = Text(Point(5,9.5),"You Win")
            userWins.setSize(20)
            userWins.setFace("courier")
            userWins.draw(win)
            game = False
    else:
        numberOfAttempts = numberOfAttempts + 1
    if (numberOfAttempts == 1):
        Head = Circle(Point(5,4.5),0.5).draw(win)
    elif (numberOfAttempts == 2):
        Body = Line(Point(5,4),Point(5,2.5)).draw(win)
    elif (numberOfAttempts == 3):
        Leg1 = Line(Point(5,2.5),Point(4.5,1.5)).draw(win)
    elif (numberOfAttempts == 4):
        Leg2 = Line(Point(5,2.5),Point(5.5,1.5)).draw(win)
    elif (numberOfAttempts == 5):
        Arm1 = Line(Point(5,3.5),Point(4.5,3)).draw(win)
    elif (numberOfAttempts == 6):
        Arm2 = Line(Point(5,3.5),Point(5.5,3)).draw(win)
        userLost = Text(Point(5,9.5),"You Lost")
        userLost.setSize(20)
        userLost.setFace("courier")
        userLost.draw(win)
        print("The correct word is", randomWord)
        game = False

win.getMouse()
win.close()