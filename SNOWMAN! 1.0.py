# Importing libraries: Time to check the efficiency of the code, nltk to provide a dictionary,
# tkinter to generate the GUI.

# import time as t
from nltk.corpus import words
from tkinter import *
from tkinter.ttk import *
import random

# Setting the variables to their default values
ChosenWord = ""

PlayAgain = True

word_list = words.words()

while PlayAgain:
    # Screen 0 Packing the GUI
    PlayAgain = False

    Play1 = False
    Play2_1 = False

    root0 = Tk()
    root0.title("SNOWMAN! 1.0")

    NrOfPlayers = 0

    Difficulty = "EASY"


    def CloseOnePlayer():
        globals()
        globals()["NrOfPlayers"] = 1
        root0.destroy()


    def CloseTwoPlayer():
        globals()
        globals()["NrOfPlayers"] = 2
        root0.destroy()


    def CloseGUI0():
        globals()
        root0.destroy()


    def EasyCommand():
        globals()["Difficulty"] = "EASY"
        MediumDifficulty["state"] = "normal"
        HardDifficulty["state"] = "normal"
        EasyDifficulty["state"] = "disabled"


    def MediumCommand():
        globals()["Difficulty"] = "MEDIUM"
        MediumDifficulty["state"] = "disabled"
        HardDifficulty["state"] = "normal"
        EasyDifficulty["state"] = "normal"


    def HardCommand():
        globals()["Difficulty"] = "HARD"
        MediumDifficulty["state"] = "normal"
        HardDifficulty["state"] = "disabled"
        EasyDifficulty["state"] = "normal"


    IntroLabel = Label(root0, text="Welcome to SNOWMAN! by LynxKhan").grid(row=0, column=0, columnspan=6)
    DifficultyLabel = Label(root0, text="Select Difficulty:").grid(row=1, column=0, columnspan=6)
    EasyDifficulty = Button(root0, text="EASY", state="disabled", command=EasyCommand)
    EasyDifficulty.grid(row=2, column=1)
    MediumDifficulty = Button(root0, text="MEDIUM", command=MediumCommand)
    MediumDifficulty.grid(row=2, column=2)
    HardDifficulty = Button(root0, text="HARD", command=HardCommand)
    HardDifficulty.grid(row=2, column=3)
    PlayLabel = Label(root0, text="Press a PLAY button to start the game.").grid(row=3, column=0, columnspan=6)
    OnePlayer = Button(root0, text="PLAY 1-Player mode", command=CloseOnePlayer).grid(row=4, column=0, columnspan=2)
    TwoPlayer = Button(root0, text="PLAY 2-Player mode", command=CloseTwoPlayer).grid(row=4, column=3, columnspan=2)
    ExitButton0 = Button(root0, text="Exit", command=CloseGUI0).grid(row=5, column=0, columnspan=6)

    root0.mainloop()

    if NrOfPlayers == 1:
        ChosenWord = word_list[random.randint(0, len(word_list) - 1)]

    if NrOfPlayers == 2:
        # Screen 1.2 Creating the GUI base element
        root1 = Tk()
        root1.title("Snowman 1.0 - 2 Players")


        def isValid(word):
            globals()
            word = word.casefold()
            if word in word_list:
                return True
            else:
                return False


        def closeGUI1_2():
            globals()
            root1.destroy()


        def PlayGame2():
            globals()
            globals()["Play2_1"] = True
            root1.destroy()


        def GetWord():
            globals()
            w_input = myEntry.get()
            if isValid(w_input):
                blanks = Label(root1,
                               text="                                                                                                    ") \
                    .grid(column=0, row=2)
                alabel = Label(root1, text="Great word! Click PLAY to begin.").grid(column=0, row=2)
                globals()["ChosenWord"] = w_input
                PlayButton["state"] = "normal"
            else:
                blanks2 = Label(root1,
                                text="                                                                                                   ").grid(
                    column=0, row=2)
                errorMessage = Label(root1, text="This word is not valid. Try another one!").grid(column=0, row=2)
                PlayButton["state"] = "disabled"


        ExitButton = Button(root1, text="Exit",
                            # fg = "red",
                            command=closeGUI1_2)

        # Creating the array of snowman pictures
        phlist = []
        for i in range(9):
            photoname = 'SM' + str(i) + '.png'
            phlist.append(photoname)
        print(phlist)

        # Screen 1.2 Packing the GUI

        TextIn = Label(master=root1, text="Write your word.").grid(column=0, row=0)
        myEntry = Entry(root1, width=100)
        myEntry.grid(column=0, row=1)
        SubmitWord = Button(root1,
                            text="Submit word",
                            command=GetWord,
                            ).grid(column=1, row=1)
        EmptySlot = Label(master=root1, text="").grid(column=0, row=2)

        PlayButton = Button(root1, text="PLAY", state="disabled", command=PlayGame2)
        PlayButton.grid(column=1, row=2)

        ExitButton.grid(column=0, row=4)

        root1.mainloop()

    if Play2_1 or NrOfPlayers == 1:  # This checks if the PLAY button has been pressed to close the previous GUI OR the 1p mode has been selected
        NrOfPlayers = 0

        SnowmanLevel = 0
        if globals()["Difficulty"] == "HARD":
            SnowmanLevel = 2


        def CloseGUI1():
            globals()
            root2.destroy()


        def PlayAgainCommand():
            globals()
            globals()["PlayAgain"] = True
            root2.destroy()


        def CheckLetter(button):
            globals()
            ButtonText = button.cget('text')
            CurrentGuess = DisplayWord["text"]
            button.config(state="disabled")
            if ButtonText in ChosenWord:
                if "_" in CurrentGuess:
                    CurrentGuessList = []
                    for n in CurrentGuess:
                        CurrentGuessList.append(n)
                    for k in range(len(ChosenWord)):
                        if ChosenWord[k] == ButtonText:
                            CurrentGuessList[2 * k + 1] = ChosenWord[k]
                    CurrentGuess = ""
                    for stringN in CurrentGuessList:
                        CurrentGuess += stringN
                    DisplayWord.config(text=CurrentGuess)
                    if not "_" in DisplayWord.cget("text"):
                        outcome.config(text="YOU WON! :D")
                        outcome.grid(row=7, column=0, columnspan=7)
                        for j in range(26):
                            LetterButtons[j].config(state="disabled")
                        PlayAgainLabel1 = Label(root2, text="Play another game?").grid(row=8, column=4)
                        PlayAgainYes1 = Button(root2, text="Yes", command=PlayAgainCommand).grid(row=8, column=5)
                        PlayAgainNo1 = Button(root2, text="No", command=CloseGUI1).grid(row=8, column=6)
            else:
                if globals()["SnowmanLevel"] < 8:
                    if globals()["Difficulty"] == "EASY":
                        globals()["SnowmanLevel"] += 1
                    else:
                        globals()["SnowmanLevel"] += 2
                SnowButtons[globals()["SnowmanLevel"]].grid(column=2, row=6, columnspan=3)
                if globals()["SnowmanLevel"] > 7:
                    LostMessage = "YOU LOST :( --- The word was " + ChosenWord
                    outcome.config(text=LostMessage)
                    outcome.grid(row=7, column=0, columnspan=7)
                    for j in range(26):
                        LetterButtons[j].config(state="disabled")
                    PlayAgainLabel1 = Label(root2, text="Play another game?").grid(row=8, column=0, columnspan=5)
                    PlayAgainYes1 = Button(root2, text="Yes", command=PlayAgainCommand).grid(row=8, column=5)
                    PlayAgainNo1 = Button(root2, text="No", command=CloseGUI1).grid(row=8, column=6)


        # Screen 2.2: Creating the GUI base element
        root2 = Tk()
        root2.title("Snowman 1.0 - Guess the word")
        ChosenWord = ChosenWord.upper()
        Instructions = Label(root2, text="This is the word you need to guess:").grid(row=0, column=0, columnspan=7)
        DisplayWord = Label(root2, text=" _" * len(ChosenWord))
        DisplayWord.grid(row=1, column=0, columnspan=7)

        # Creating the snowman pictures
        # Create a different button for each snowman stage. Not elegant, but hey.
        SnowButtons = []
        for i in range(9):
            SnowButtons.append([])

        photoname = []
        for i in range(9):
            photoname.append(PhotoImage(master=root2, file='SM' + str(i) + '.png'))
            # PhotoImage(file=phlist[5])
            SnowButtons[i] = Button(root2,
                                    # text="Confirm word",
                                    image=photoname[i],
                                    # state=DISABLED,
                                    width=5,
                                    command=None,
                                    # fg = "white",
                                    # bg = "navy",
                                    )

        # Creating a button for each letter.
        LetterButtons = []
        butA = Button(root2, text="A", command=lambda: CheckLetter(butA))
        butA.grid(row=2, column=0)
        LetterButtons.append(butA)
        butB = Button(root2, text="B", command=lambda: CheckLetter(butB))
        butB.grid(row=2, column=1)
        LetterButtons.append(butB)
        butC = Button(root2, text="C", command=lambda: CheckLetter(butC))
        butC.grid(row=2, column=2)
        LetterButtons.append(butC)
        butD = Button(root2, text="D", command=lambda: CheckLetter(butD))
        butD.grid(row=2, column=3)
        LetterButtons.append(butD)
        butE = Button(root2, text="E", command=lambda: CheckLetter(butE))
        butE.grid(row=2, column=4)
        LetterButtons.append(butE)
        butF = Button(root2, text="F", command=lambda: CheckLetter(butF))
        butF.grid(row=2, column=5)
        LetterButtons.append(butF)
        butG = Button(root2, text="G", command=lambda: CheckLetter(butG))
        butG.grid(row=2, column=6)
        LetterButtons.append(butG)
        butH = Button(root2, text="H", command=lambda: CheckLetter(butH))
        butH.grid(row=3, column=0)
        LetterButtons.append(butH)
        butI = Button(root2, text="I", command=lambda: CheckLetter(butI))
        butI.grid(row=3, column=1)
        LetterButtons.append(butI)
        butJ = Button(root2, text="J", command=lambda: CheckLetter(butJ))
        butJ.grid(row=3, column=2)
        LetterButtons.append(butJ)
        butK = Button(root2, text="K", command=lambda: CheckLetter(butK))
        butK.grid(row=3, column=3)
        LetterButtons.append(butK)
        butL = Button(root2, text="L", command=lambda: CheckLetter(butL))
        butL.grid(row=3, column=4)
        LetterButtons.append(butL)
        butM = Button(root2, text="M", command=lambda: CheckLetter(butM))
        butM.grid(row=3, column=5)
        LetterButtons.append(butM)
        butN = Button(root2, text="N", command=lambda: CheckLetter(butN))
        butN.grid(row=3, column=6)
        LetterButtons.append(butN)
        butO = Button(root2, text="O", command=lambda: CheckLetter(butO))
        butO.grid(row=4, column=0)
        LetterButtons.append(butO)
        butP = Button(root2, text="P", command=lambda: CheckLetter(butP))
        butP.grid(row=4, column=1)
        LetterButtons.append(butP)
        butQ = Button(root2, text="Q", command=lambda: CheckLetter(butQ))
        butQ.grid(row=4, column=2)
        LetterButtons.append(butQ)
        butR = Button(root2, text="R", command=lambda: CheckLetter(butR))
        butR.grid(row=4, column=3)
        LetterButtons.append(butR)
        butS = Button(root2, text="S", command=lambda: CheckLetter(butS))
        butS.grid(row=4, column=4)
        LetterButtons.append(butS)
        butT = Button(root2, text="T", command=lambda: CheckLetter(butT))
        butT.grid(row=4, column=5)
        LetterButtons.append(butT)
        butU = Button(root2, text="U", command=lambda: CheckLetter(butU))
        butU.grid(row=4, column=6)
        LetterButtons.append(butU)
        butV = Button(root2, text="V", command=lambda: CheckLetter(butV))
        butV.grid(row=5, column=1)
        LetterButtons.append(butV)
        butW = Button(root2, text="W", command=lambda: CheckLetter(butW))
        butW.grid(row=5, column=2)
        LetterButtons.append(butW)
        butX = Button(root2, text="X", command=lambda: CheckLetter(butX))
        butX.grid(row=5, column=3)
        LetterButtons.append(butX)
        butY = Button(root2, text="Y", command=lambda: CheckLetter(butY))
        butY.grid(row=5, column=4)
        LetterButtons.append(butY)
        butZ = Button(root2, text="Z", command=lambda: CheckLetter(butZ))
        butZ.grid(row=5, column=5)
        LetterButtons.append(butZ)

        SnowButtons[0].grid(column=2, row=6, columnspan=3)

        outcome = Label(root2, text="")
        outcome.grid(row=7, column=0, columnspan=7)

        root2.mainloop()
