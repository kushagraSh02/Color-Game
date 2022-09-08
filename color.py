import tkinter
import random

colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score=0
timeleft=30

def startGame(event):
    if timeleft==30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft

    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1

        e.delete(0, tkinter.END)
        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text='Score: '+str(score))

def countdown():
            global timeleft
            if timeleft>0:
                timeleft-=1
                timeLabel.config(text='Time left: '+str(timeleft))
                timeLabel.after(1000, countdown)

root=tkinter.Tk()

root.title('ColorGame')
root.geometry('300x500')
instructions=tkinter.Label(root, text='Type in the color'
                           'of the word, not the text!',
                           font=('sans serif', 12))
instructions.pack()

scoreLabel=tkinter.Label(root, text='Press Enter to start',
                         font=('sans serif', 12))
scoreLabel.pack()

timeLabel=tkinter.Label(root, text='Time left: '+
                        str(timeleft), font=('sans serif', 12))
timeLabel.pack()

label=tkinter.Label(root, font=('sans serif', 60))
label.pack()

e=tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()
root.mainloop()