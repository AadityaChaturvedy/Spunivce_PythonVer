import random
import os

print('\n')
print("This is a random word picker game, enter 3 word and the system will pick one for you")
z=random.randint(1,3)
print('\n')
a=input("Enter first word:")
print('\n')
b=input("Enter second word:")
print('\n')
c=input("Enter third word:")
d='The Word Choosen is:'
for j in range(1):
       if(z == 1):
              print(d,a)
       elif(z == 2):
              print(d,b)
       elif(z == 3):
              print(d,c)
os.system('python Start.py')