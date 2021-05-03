import os


def Begin():
    print("\n")
    print("What would you like to do:- Use Utilities(UT), Play Games(PG), Delete Account(DA) or Exit")
    z=input()
    
    if(z == "UT"):
        Utilities()
    elif(z == "PG"):
        Game()
    elif(z == "DA"):
        os.system('python Deleteaccount.py')
    elif(z == "Exit"):
        print("ThankYou For Using the App")
        input('Press Enter To Exit')
        quit()
        
    if(z != 'UT', z!= 'PG', z!= 'Exit'):
        print('Enter Correct Code')
        Begin()

def TakeInputUT():
    l = input("Choose what you want to open:")
    if(l == 'NQ'):
        os.system('python Newquan.py')
    elif(l == 'ME'):
        os.system('python Equation.py')
    elif(l == 'PG'):
        os.system('python PasswordGenerator.py')

    if(l != 'NQ', l != 'ME', l != 'PG', l != 'UT', l!= 'PG'):
        print('Enter Correct Code')
        Begin()

def TakeInputGA():
    l = input("Choose what you want to open:")
    if(l == 'RWG'):
        os.system('python RandomWord.py')
    elif(l == 'RN'):
        os.system('python RandomNum.py')
    elif(l == 'TP'):
        os.system('python TimePass.py')

    if(l != 'RWG', l != 'RN', l != 'TP'):
        print('Enter Correct Code')
        Begin()
    

def Utilities():
    print("\n")
    print("The Available option of utilities are: NewQuan(NQ), PasswordGenerator(PG) and MathsEquation(ME)")
    TakeInputUT()

def Game():
    print("\n")
    print("The Available option of games are:- Random Word Generator(RWG), RandomNum(RN) and TimePass(TP)")
    TakeInputGA()

Begin()
