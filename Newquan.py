import os

space = '\n'
print('Welcome To NewQuan')
print(space)
nosud=int(input("Enter the number of students:"))
answerset=[]
print(space)
noques=int(input("enter the number of question:"))
for i in range(0,noques):
        print(space)
        print("enter the anwers of option",i+1)
        print(space)
        c=input("enter the option number:")
        answerset.append(c)
for i in range(1,1001):
        print("storing data",i//10,"%")
result={}
for i in range(0,nosud):
        ca=0
        print(space)
        name=input("enter the name of the student:")
        sutans=[]
        for i in range(0,len(answerset)):
                print(space)
                print("Enter the answer of",i+1,":")
                print(space)
                anssut=input("Enter the answer:") 
                sutans.append(anssut)
                if answerset[i]==sutans[i]:
                        ca+=1
        result[name]=ca
print(space)
con=input("Should I print result:")
if con=="yes":
        print(space)
        print(result)
if con=="no":
        print(space)
        print("why did you waste my time sucker")

os.system('python Start.py')