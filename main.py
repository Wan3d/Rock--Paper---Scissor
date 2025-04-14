import tkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import random
import winsound

# Creating variables
contComputerWin = 0
contUserWin = 0

# Create window
window = tk.Tk()
window.title("Rock, Paper & Scissor")
window.configure(background="black")
window.geometry("800x500")

# Updating choice
def updateChoice(userSelection):
    userSelectionLabel.place(relx=0.2, rely=0.4, anchor='center')
    computerSelectionLabel.place(relx=0.8, rely=0.4, anchor='center')

    if userSelection == "Rock":
        userSelectionLabel.config(text="✊", fg='red')
        computerSelection = computerChoice()
        convertEmoji(computerSelection)
    elif userSelection == "Paper":
        userSelectionLabel.config(text="✋", fg='blue')
        computerSelection = computerChoice()
        convertEmoji(computerSelection)
    elif userSelection == "Scissor":
        userSelectionLabel.config(text="✌️", fg='green')
        computerSelection = computerChoice()
        convertEmoji(computerSelection)

    comparisionMethod(userSelection, computerSelection)

# Convert selection to emoji
def convertEmoji(computerSelection):
    if computerSelection == "Rock": 
        computerSelectionEmoji = "✊"
        computerSelectionLabel.config(text=computerSelectionEmoji, fg='red')
    elif computerSelection == "Paper": 
        computerSelectionEmoji = "✋"
        computerSelectionLabel.config(text=computerSelectionEmoji, fg='blue')
    elif computerSelection == "Scissor": 
        computerSelectionEmoji = "✌️"
        computerSelectionLabel.config(text=computerSelectionEmoji, fg='green')

# Comparision method
def comparisionMethod(userSelection, computerSelection):
    global contComputerWin
    global contUserWin

    # Rock loss -> Paper
    # Rock win -> Scissor
    if userSelection == "Rock":
        if computerSelection == "Paper": contComputerWin += 1
        elif computerSelection == "Scissor": contUserWin += 1
    # Paper loss -> Scissor
    # Paper win -> Rock
    elif userSelection == "Paper":
        if computerSelection == "Scissor": contComputerWin += 1
        elif computerSelection == "Rock": contUserWin += 1
    # Scissor loss -> Rock
    # Scissor win -> Paper
    elif userSelection == "Scissor":
        if computerSelection == "Rock": contComputerWin += 1
        elif computerSelection == "Paper": contUserWin += 1

    userContLabel.config(text=f"Player Score: {contUserWin}")
    computerContLabel.config(text=f"CPU Score: {contComputerWin}")

# Computer choice method
def computerChoice():
    choices = ["Rock", "Paper", "Scissor"]
    choiceRandom = random.randint(0,2)

    if choices[choiceRandom] == "Rock":
        choiceSelected = "Rock"
    elif choices[choiceRandom] == "Paper":
        choiceSelected = "Paper"
    elif choices[choiceRandom] == "Scissor":
        choiceSelected = "Scissor"
    return choiceSelected

# Creating label
userSelectionLabel = Label(window, background='black', fg='white', font=('Times New Roman', 70))
computerSelectionLabel = Label(window, background='black', fg='white', font=('Times New Roman', 70))

userContLabel = Label(window, background='black', fg='white', text=f"Player Score: {contUserWin}", font=('Times New Roman', 16))
userContLabel.place(relx=0.2, rely=0.1, anchor='center')

computerContLabel = Label(window, background='black', fg='white', text=f"CPU Score: {contComputerWin}", font=('Times New Roman', 16))
computerContLabel.place(relx=0.8, rely=0.1, anchor='center')

# Create Rock, Paper & Scissor buttons and place them
rockButton = Button(window,
                    command=lambda:updateChoice("Rock"),
                    text='Rock',
                    height=5, 
                    width=15, 
                    bg='red').place(relx=0.3,
                                    rely=0.8, 
                                    anchor='center')
paperButton = Button(window, 
                    text='Paper',
                    command=lambda:updateChoice("Paper"),
                    height=5,
                    width=15,
                    bg='blue').place(relx=0.5,
                                    rely=0.8,
                                    anchor='center')
scissorButton = Button(window, 
                    text='Scissor',
                    command=lambda:updateChoice("Scissor"),
                    height=5,
                    width=15,
                    bg='green').place(relx=0.7,
                                    rely=0.8,
                                    anchor='center')

# Dispose window
window.mainloop()

