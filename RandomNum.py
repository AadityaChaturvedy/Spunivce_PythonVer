import random
import os

print("\n""This is a number guessing game you wil get 5 turns, the number is random")
z=random.randint(1,50)
x=random.randint(50,100)
i=random.randint(z,x)
for j in range(1,6):
       a=int(input("Enter the guess:"))
       if(a>i):
              print(a,"Is bigger than the number","\n")
       elif(a<i):
              print(a,"Is lesser than the number","\n")
       elif(a==i):
              print("Congtrats you guessed the correct number it was",i,"\n")
              break
if(a!=i):
       print("Bad luck the number was",i,"\n")
print("The number was chosen between the interval",z,x)

os.system('python Start.py')
