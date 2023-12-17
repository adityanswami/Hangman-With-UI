# import random
import random
# import tkinter
import tkinter

from tkinter import messagebox

from functools import partial

levelWindow = tkinter.Tk()
checkVar = tkinter.IntVar()

levelWindow.iconbitmap("icon.ico")

def game(levelInput):
    global checkVar
    global hangmanCanvas
    global gameWindow
    gameWindow = tkinter.Toplevel()
    gameWindow.title("Game window")
    gameWindow.geometry("1000x500+100+100")
    gameWindow.config(bg="#c1dbb3")

    hangmanCanvas = tkinter.Canvas(gameWindow, height=500, width=300, bg="#a1cea9")
    hangmanCanvas.place(x=0, y=0)

    # choose a correctAnswer from the list of languages randomly
    correctAnswer = getWord(levelInput).strip()
    # create a list variable which will hold the current state of the user answer
    currentState = ["~"] * len(correctAnswer)
    # set an incorrectGuessCounter to 0
    incorrectGuessCounter = 0
    # set a countLettersLeft to length of correctAnswer
    countLettersLeft = len(correctAnswer)
    # create list with list of letters guessed
    lettersGuessed = []
    currentStateLabel = tkinter.Label(gameWindow, text="".join(currentState), font=("Calibri", 35), bg="#f3c584",
                                      fg="black")

    currentStateLabel.place(x=350, y=50)
    guessEntryLabel = tkinter.Label(gameWindow, text="Guess a letter: ", font=("Calibri", 30), bg="#c1dbb3",
                                    fg="black")
    guessEntryLabel.place(x=350, y=120)
    guessEntryField = tkinter.Entry(gameWindow, font=("Calibri", 30))
    guessEntryField.place(x=350, y=200)
    guessOkButton = tkinter.Button(gameWindow, text="OK", bg="#f3c584", fg="black", font=("Calibri", 30),
                                   command=lambda: checkVar.set(1))
    guessOkButton.place(x=600, y=300)
    # while the countLettersLeft is not 0 and the incorrectGuessCounter is not 8
    while (countLettersLeft != 0) and (incorrectGuessCounter != 8):

        # set a condition variable(T / F) for whether user has guessed letter as True
        alrGuessed = True
        # initialize trigger 1
        trigger1 = True
        # while the user has already guessed the letter

        while alrGuessed:
            guessEntryField.focus()
            # ask user for a guess
            guessOkButton.wait_variable(checkVar)
            guess = guessEntryField.get()
            guessEntryField.delete(0, tkinter.END)
            checkVar.set(0)
            # if nothing has been guessed, set the T / F variable to false
            if len(lettersGuessed) == 0:
                alrGuessed = False
            # else
            else:
                # check if user has already entered this guess(for loop)
                for letter in lettersGuessed:

                    # if the user has entered the letter already
                    if letter == guess:
                        messagebox.showinfo("Letter Already Guessed", "The letter " + guess + " has already been guessed", parent=gameWindow)

                        alrGuessed = True
                        # break
                        break
                    # else
                    else:
                        # set the variable to False
                        alrGuessed = False
                        guessEntryField.delete(0, tkinter.END)
        # add the guess to the list of answers guessed
        lettersGuessed.append(guess)

        # Next, check if the guess matches any letter in the correctAnswer (for loop, for i in range(len(correctAnswer))
        for i in range(len(correctAnswer)):
            # if the guess is equal to the index value of the correctAnswer
            if guess == correctAnswer[i]:
                # change that index of the current state of answer variable to the correctAnswer / guess
                currentState[i] = guess
                # trigger1 should be False
                trigger1 = False
                # countLettersLeft decreases by one
                countLettersLeft -= 1
        # if trigger 1 is true:
        if trigger1:
            # incorrectGuessCounter is increased by 1
            incorrectGuessCounter += 1
        # if incorrectGuessCounter is 1 and trigger1:
        if incorrectGuessCounter == 1 and trigger1:
            # draw the gallows
            gallows()
        # elif incorrectGuessCounter is 2 and trigger1:
        elif incorrectGuessCounter == 2 and trigger1:
            # draw the noose
            noose()
        # elif incorrectGuessCounter is 3 and trigger1:
        elif incorrectGuessCounter == 3 and trigger1:
            # draw the head
            head()
        # elif incorrectGuessCounter is 4 and trigger1:
        elif incorrectGuessCounter == 4 and trigger1:
            # draw the body
            body()
        # elif incorrectGuessCounter is 5 and trigger1:
        elif incorrectGuessCounter == 5 and trigger1:
            # draw the right arm
            rightArm()
        # elif incorrectGuessCounter is 6 and trigger1:
        elif incorrectGuessCounter == 6 and trigger1:
            # draw the left arm
            leftArm()
        # elif incorrectGuessCounter is 7 and trigger1:
        elif incorrectGuessCounter == 7 and trigger1:
            # draw the right leg
            rightLeg()
        # elif incorrectGuessCounter is 8 and trigger1:
        elif incorrectGuessCounter == 8 and trigger1:
            # draw the left leg
            leftLeg()
        # print the current state of answer
        gameWindow.update()
        currentStateLabel['text'] = "".join(currentState)
        gameWindow.update()

    # if the incorrectGuessCounter is 8:
    if incorrectGuessCounter == 8:
        currentStateLabel['text'] = correctAnswer
        gameWindow.update()
        messagebox.showinfo("Game Lost!", "Sorry! You lose!", parent=gameWindow)
        # hangmanCanvas.create_line()
        gameWindow.destroy()
    # elif the countLettersLeft is 0:
    elif countLettersLeft == 0:
        # print that user won
        messagebox.showinfo("You win!", "Congratulations! You win!", parent=gameWindow)
        gameWindow.destroy()
    currentStateLabel.destroy()

# define a function to draw the gallows pole(t)
def gallows():
    hangmanCanvas.create_line("0.5i", "5i", "0.5i", "0.5i", width=5)
    hangmanCanvas.create_line("0.5i", "1.25i", "1.25i", "0.5i", width=5)
    hangmanCanvas.create_line("0.5i", "0.5i", "1.5i", "0.5i", width=5)


# define a function to draw the noose(t)
def noose():
    hangmanCanvas.create_line("1.5i", "0.5i", "1.5i", "1i", width=3)

# define a function to draw the head(t)
def head():
    hangmanCanvas.create_oval("1i", "1i", "2i", "2i", width=5)

# define a function to draw the body(t)
def body():
    hangmanCanvas.create_line("1.5i", "2i", "1.5i", "4i", width=5)

# define a function to draw right arm(t)
def rightArm():
    hangmanCanvas.create_line("1.5i", "2.75i", "1i", "3.1i", width=5)

# define a function to draw left arm(t)
def leftArm():
    hangmanCanvas.create_line("1.5i", "2.75i", "2i", "3.1i", width=5)

# define a function to draw right leg(t)
def rightLeg():
    hangmanCanvas.create_line("1.5i", "4i", "1i", "4.35i", width=5)

# define a function to draw left leg(t)
def leftLeg():
    hangmanCanvas.create_line("1.5i", "4i", "2i", "4.35i", width=5)


# gets a word from the relevant file
def getWord(levelInput):
    # Creates a list which will store the lines of the file
    lines = []
    # opens the text file with the words in a variable
    text_file = open("level" + levelInput + ".txt", "r")
    # puts all the lines of the file (1 line per word)
    linesAsInFile = text_file.readlines()
    # to standardize all the words into lowercase, for loop appending the lowercase form of each word to new list
    for line in linesAsInFile:
        lines.append(line.lower())
    # closes the text file
    text_file.close()
    correctAnswer = random.choice(lines)
    return correctAnswer

hangmanLabel = tkinter.Label(levelWindow, text="Hangman!", bg="#c1dbb3", fg="black", font=("Calibri", 40))
hangmanLabel.place(x=350, y=50)
levelPickLabel = tkinter.Label(levelWindow, text="Pick your level", bg="#c1dbb3", fg="black", font=("Calibri", 20))
levelPickLabel.place(x=370, y=150)
fontForButtons = ("Calibri", 16)
level1Button = tkinter.Button(levelWindow, text="Level 1", bg="#f3c584", fg="black", font=fontForButtons,
                              command=partial(game, "1"))
level1Button.place(x=400, y=200)
level2Button = tkinter.Button(levelWindow, text="Level 2", bg="#f3c584", fg="black", font=fontForButtons,
                              command=partial(game, "2"))
level2Button.place(x=400, y=250)
level3Button = tkinter.Button(levelWindow, text="Level 3", bg="#f3c584", fg="black", font=fontForButtons,
                              command=partial(game, "3"))
level3Button.place(x=400, y=300)
level4Button = tkinter.Button(levelWindow, text="Level 4", bg="#f3c584", fg="black", font=fontForButtons,
                              command=partial(game, "4"))
level4Button.place(x=400, y=350)
level5Button = tkinter.Button(levelWindow, text="Level 5", bg="#f3c584", fg="black", font=fontForButtons,
                              command=partial(game, "5"))
level5Button.place(x=400, y=400)
levelWindow.title("Hangman")
levelWindow.geometry("1000x500+100+100")
levelWindow.config(bg="#c1dbb3")
levelWindow.mainloop()









