import random
import os

global sma
global num
caplist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
smallist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numlist=['0','1','2','3','4','5','6','7','8','9']
caplenght=len(caplist)
smalenght=len(smallist)
numlenght=len(numlist)
capnum=random.randint(0,(caplenght-1))
cap=caplist[capnum]
password=''
for i in range(0,4):
        smanum=random.randint(0,(smalenght-1))
        numnum=random.randint(0,(numlenght-1))
        sma=smallist[smanum]
        num=numlist[numnum]
        password=password+sma+num
password=cap+'@'+password
print("Your highly secured generated password is:",password)

os.system('Start.py')
