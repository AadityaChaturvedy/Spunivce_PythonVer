import tkinter

import random as r

import os

global timeleft

global num1

global user

global num2

global zero

global sign

global answer

global equation

global score

root=tkinter.Tk()


numlist=['1','2','3','4','5','6','7','8','9','11','12','13','15','14','1','3','10','10','3','5',]

signlist=['+','+','+','-','-','*','*','/','%','**']

expolist=('2','3')

score=0

timeleft=150

answer=0

user=0

useranswer=tkinter.Entry(root)

def startGame(event):
    global timeleft 

    if timeleft == 150: 
        countdown()
        
        equations()
        
        answers() 

    next()

root.bind('<Return>', startGame)

def equations():
    global score

    global timeleft

    global answer

    global reanum1

    global reanum2

    global sign

    global equation

    global user

    global num1

    global num2

    global expo

    num1=r.choice(numlist)

    num2=r.choice(numlist)

    sign=r.choice(signlist)

    expo=r.choice(expolist)
    
    if sign=='**':
        equation=num1+sign+expo
    
    else:
        equation=num1+sign+num2

    reanum1=int(num1)

    reanum2=int(num2)

    label1.config(self,text=str(equation))

    answers()


def answers():

    global sign

    global answer

    if sign=='+':
        answer=reanum1+reanum2
    
    elif sign=='*':
        answer=reanum1*reanum2
    
    elif sign=='-':
        answer=reanum1-reanum2
    
    elif sign=='/':
        answer=reanum1//reanum2
    
    elif sign=="**":
        answer=reanum1**int(expo)
    elif sign=='%':
        answer=reanum1%reanum2

def next():
    global score
    
    global user
    
    global timeleft
    
    global answer
    
    if timeleft>0:
        useranswer.focus_set()
        
        if useranswer.get()==str(answer):
            
            if sign=="**":
                score=score+10
            
            elif sign=="%" or sign=="/":
                score+=5
            
            elif sign=="*":
                score+=2
            
            else:    
                score=score+1  

    useranswer.delete(0, tkinter.END)
    
    scorelabel.config(text="score= "+str(score))
    
    equations()
    
    answers()

a=0

def countdown(): 

    global timeleft 

    global a

    if timeleft > 0: 
        timeleft -= 1    
        timeLabel.config(text = "Time left: "+ str(timeleft)) 
        timeLabel.after(1000, countdown)
    
    if timeleft==0:
    
        for i in range(1,10000000):
            a+=1        
    
        root.destroy()
        os.system('python Start.py')

scorelabel =tkinter.Label(root,text="press enter to start",font = ('Helvetica', 12)) 
scorelabel.pack() 

timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

label1=tkinter.Label(root,font=('Helvetica', 60))
self=label1
label1.pack()
 
useranswer.pack()

root.mainloop()