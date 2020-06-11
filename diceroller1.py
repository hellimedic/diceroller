#aliceroller

from tkinter import *
import random
import os
import subprocess
from functools import partial


# this opens up a file called rolls.txt. the 'w' flag means its writable.
# i need to do a time/date stamp, then put all the d20 rolls into it
# this needs work - need to add newline after each
# also need to figure out timestamp
# can use os.system(date) to get the date and time

with open('rolls.txt', 'w') as f:
    data = ' some data stuff'
    f.write(data)
    f.write(data)
    f.write(data)
    f.write(data)
    f.write("\nRAHRAHRAHRAHRAHRAH\n")



# import pyttsx3

# this is a simple function, takes in an integer, does a random roll, outputs the
# result, which is an integer between 1 and r, which is the number passed
# dice(6) will return an integer between 1 and 6


def dice(r):
    roll = random.randint(1, r)
    return(roll)


# this list just stores all the attack rolls and can be echoed to the command line

attackRollsList = []




def go():

    cs = damageDiceListbox.curselection()[0]
    #intCs = int(cs)
    damageDiceLabel['text'] = damageDiceListbox.get(cs)
""" this function looks at the cursor selection in the damage dice listbox
and turns it into an integer.  it also changes the label of the damage dice
listbox into the selected option.  
this same system is used for calculating the damage roll later

    """


def randomRoll(r):
    roll = dice(r)
    # this logger command is just so the console shows what happens.
    # logger = "echo " + str(roll)
    # os.system(logger)
    roll_speak(roll)
    labelRandomRoll.configure(text = roll)
""" this function is supposed to let the user make a random roll clicking one of
the buttons at the bottom of the screen.
"""


def attackClicked():
    # this is for damage calculating, it doesn't work  yet
    global CRITHIT
    # this gets what the user entered for modifiers and turns it into integers
    # and then it is used later in the rolling
    #resetting the values to what the user enters
    
    _userProfBonus = profEntry.get()
    _userProfInt = int(_userProfBonus)
    _userStatBonus = statEntry.get()
    _userStatInt = int(_userStatBonus)
    _userMagicBonus = magicEntry.get()
    _userMagicInt = int(_userMagicBonus)

    _attackRoll = dice(20)
    attackRollsList.append(_attackRoll)
    if _attackRoll == 20:
        os.system("say critical hit")
        CRITHIT = 1
    _attackSpeak = "say rolled" + str(_attackRoll)
    attackRolled.configure(text = _attackRoll)
    _attackRollFinal = _attackRoll + _userProfInt + _userStatInt + _userMagicInt
    _attackspeak2 = "say final attack" + str(_attackRollFinal)
    attackRolledFinal.configure(text = _attackRollFinal)
    labelAllAttackRolls.configure(text = attackRollsList)
    os.system(_attackSpeak)
    os.system(_attackspeak2)
    _echoCommand = "echo " + str(attackRollsList)
    # os.system(_echoCommand)

    damageRoll()


# this function takes a number and speaks it out.
# currently this function uses os.system which only works on MACOS.
# need to figure out a text to speech that can be dropped in here


def roll_speak(int):
    # take the number, add to say command
    _rollSpeak = "say " + str(int)
    os.system(_rollSpeak)


def damageRoll():
    _userProfBonus = profEntry.get()
    _userProfInt = int(_userProfBonus)
    _userStatBonus = statEntry.get()
    _userStatInt = int(_userStatBonus)
    _userMagicBonus = magicEntry.get()
    _userMagicInt = int(_userMagicBonus)

    cs = damageDiceListbox.curselection()[0]
    intCs = int(cs)
    damageDiceItems = [4, 6, 8, 10, 12]
    _damageRoll = dice(damageDiceItems[intCs])
    damageRolledDice.configure(text = _damageRoll)
    _damageSpeak = "say damage roll " + str(_damageRoll)
    _finalDamage = _damageRoll + _userStatInt + _userMagicInt
    damageRolledOutput.configure(text = _finalDamage)
    _finalDamageSpeak = "say final damage " + str(_finalDamage)
    os.system(_damageSpeak)
    os.system(_finalDamageSpeak)


def initiativeRoll():
    _userInitiativeBonus = initEntry.get()
    _userInitiativeInt = int(_userInitiativeBonus)
    _initiativeRollOutput = dice(20) + _userInitiativeInt
    echoroll = "echo " + str(_initiativeRollOutput)
    os.system(echoroll)
    roll_speak(_initiativeRollOutput)
    initiativeRollFinal.configure(text = _initiativeRollOutput)


window = Tk()

window.title("Diceroller GUI")
window.geometry('800x800')

# had to comment out the color, it looks garish
# window['bg'] = 'gray78'

profLabel = Label(window, bg = "cyan", text = "Proficiency Bonus")
profLabel.grid(column = 1, row = 1)
profEntry = Entry(window, bg = "cyan", bd = 3, width = 5)
profEntry.grid(column = 2, row = 1)
profEntry.insert(END, '0')

statLabel = Label(window, bg = "cyan", text = "Attack stat modifier")
statLabel.grid(column = 1, row = 3)
statEntry = Entry(window, bg = "cyan", bd = 3, width = 5)
statEntry.grid(column = 2, row = 3)
statEntry.insert(END, '0')

magicLabel = Label(window, bg = "cyan", text = "Magic Weapon Bonus")
magicLabel.grid(column = 1, row = 5)
magicEntry = Entry(window, bg = "cyan", bd = 3, width = 5)
magicEntry.grid(column = 2, row = 5)
magicEntry.insert(END, '0')

initiativeLabel = Label(window, bg = "red", text = "enter initiative modifier")
initiativeLabel.grid(column = 4, row = 1)
initEntry = Entry(window, bd = 3, bg = "red", width = 5)
initEntry.grid(column = 5, row = 1)
initEntry.insert(END, '0')

initiativeFinal = Label(window, bg = "red", text = "rolled")
initiativeFinal.grid(column = 4, row = 3)
initiativeRollFinal = Label(window, bg = "red", text = "##")
initiativeRollFinal.grid(column = 5, row = 3)
initiativeButton = Button(window, text = "Roll initaitive", height = 2, width = 12, font = 'Helvetica 18 bold', fg = "red", bg = "blue", command = initiativeRoll)
initiativeButton.grid(column = 4, row = 5)

damageDiceLabel = Label(window, bg = "cyan", text = "Dice")
damageDiceLabel.grid(column = 1, row = 7)

damageDiceListbox = Listbox(window, bg = "cyan")

damageDiceItems = [4, 6, 8, 10, 12]
for item in damageDiceItems:
    damageDiceListbox.insert(END, item)

damageDiceListbox.grid(column = 2, row = 7)
damageDiceListbox.config(width =5, height = 7)
damageDiceListbox.bind("<<ListboxSelect>>", lambda x: go())

attackLabel = Label(window, text = "Roll")
attackLabel.grid(column = 2, row = 8)
modifiedLabel = Label(window, text = "Final result")
modifiedLabel.grid(column =3, row = 8)

attackButton = Button(window, text = "roll attack", height = 2, width = 12, font = 'Helvetica 18 bold', command = attackClicked)
attackButton.grid(column = 1, row = 9)
attackRolled = Label(window, text = " ")
attackRolled.grid(column = 2, row = 9)
attackRolledFinal = Label(window, text = " ")
attackRolledFinal.grid(column = 3, row = 9)

damageRolled = Label(window, text = "Damage")
damageRolled.grid(column = 1, row = 11)
damageRolledDice = Label(window, text = "#")
damageRolledDice.grid(column = 2, row = 11)
damageRolledOutput = Label(window, text = "#")
damageRolledOutput.grid(column = 3, row = 11)

labelRandomRoll = Label (window, fg = "green", height = 1, width = 5, font = "Helvetica 48 bold", text =  "##")
labelRandomRoll.grid(column = 3, row = 15)

# i used the echo on the command line in the randomRoll function to
# track what was happening. what i found was that when calling a function
# on a button WITH a variable (4, 6, 8 etc) is that it would run immediately
# when the form was loaded.  and pushing the button did nothing
# i found stack overflow which explained to do it with "partial"
# which i don't understand at all.  but, it works.  need to learn what it does

#Or even shorter: button = Tk.Button(master=frame, text='press', command=partial(action, arg))

#this is my old button code
# d4Button = Button(window, text = "D4", command = randomRoll(4))

dice_btn_style = dict(fg = "green", height = 2, width = 5, font = 'Helvetica 18 bold')


d4Button = Button(window, text = "D4",command = partial(randomRoll, 4), **dice_btn_style)
d4Button.grid(column = 1, row = 13)
d6Button = Button(window, text = "D6", command = partial(randomRoll, 6), **dice_btn_style)
d6Button.grid(column = 1, row = 14)
d8Button = Button(window, text = "D8", command = partial(randomRoll, 8), **dice_btn_style)
d8Button.grid(column = 1, row = 15)
d10Button = Button(window, text = "D10", command = partial(randomRoll, 10), **dice_btn_style)
d10Button.grid(column = 1, row = 16)
d12Button = Button(window, text = "D12", command = partial(randomRoll, 12), **dice_btn_style)
d12Button.grid(column = 1, row = 17)
d20Button = Button(window, text = "D20", command = partial(randomRoll, 20), **dice_btn_style)
d20Button.grid(column = 1, row = 18)

labelAllAttackRolls = Label(window, text = "##", width = 40)
labelAllAttackRolls.grid(column = 3, row = 20)

    # engine = pyttsx3.init()
    # engine.say("hello crazy programmer")
    # engine.setProperty('rate',120)
    # engine.setProperty('volume', 0.9)
    # engine.runAndWait()

# engine = pyttsx3.init()
# engine.runAndWait()
window.mainloop()






