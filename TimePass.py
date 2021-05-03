from tkinter import *
import os

root = Tk()

def Pattern1():
	for i in range(1,6):
		print(" ")
		for j in range(1,i+1):
			print("*",end=" ")
	for i in range(1,4):
		print("  ")		

def Pattern2():
	for i in range(1,6):
		print(" ")
		for j in range(1,i+1):
			print(i,end=" ")
	for i in range(1,4):
		print("  ")	

def Pattern3():
	for i in range(1,6):
		print(" ")
		for j in range(1,i+1):
			print(j,end=" ")
	for i in range(1,4):
		print("  ")	

def Pattern4():
	for i in range(5,0,-1):
		print(" ")
		for j in range(i,0,-1):
			print("*",end=" ")
	for i in range(1,4):
		print("  ")			

def Pattern5():
	for i in range(5,0,-1):
		print(" ")
		for j in range(i,0,-1):
			print(i,end=" ")
	for i in range(1,4):
		print("  ")	

def Pattern6():
	for i in range(5,0,-1):
		print(" ")
		for j in range(i,0,-1):
			print(j,end=" ")
	for i in range(1,4):
		print("  ")

def Pattern7():
        root.destroy()
        os.system('python Start.py')

mybutton1=Button(root,text="Click me",command=Pattern1)

mylabel1=Label(root,text="Pattern with*")

mybutton2=Button(root,text="Click me",command=Pattern2)

mylabel2=Label(root,text="Pattern with numbers one")

mybutton3=Button(root,text="Click me",command=Pattern3)

mylabel3=Label(root,text="Pattern with coutinuous number")

mybutton4=Button(root,text="Click me",command=Pattern4)

mylabel4=Label(root,text="Reverse of 1")

mybutton5=Button(root,text="Click me",command=Pattern5)

mylabel5=Label(root,text="Reverse of 2")

mybutton6=Button(root,text="Click me",command=Pattern6)

mylabel6=Label(root,text="Reverse of 3")

mybutton7=Button(root,text="Click me",command=Pattern7)

mylabel7=Label(root,text="Finish")

mylabel1.pack()

mybutton1.pack()

mylabel2.pack()

mybutton2.pack()

mylabel3.pack()

mybutton3.pack()

mylabel4.pack()

mybutton4.pack()

mylabel5.pack()

mybutton5.pack()

mylabel6.pack()

mybutton6.pack()

mylabel7.pack()

mybutton7.pack()

root.mainloop()
