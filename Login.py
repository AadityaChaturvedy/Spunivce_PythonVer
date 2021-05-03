import mysql.connector
import string
import os
import csv
import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        begin()
        access(option)
    except:
        print('Connect To Internet To Login')
        

def Login(name,password):

    global success
    
<<<<<<< Updated upstream
    connection = mysql.connector.connect(host = 'sql12.freesqldatabase.com',database = 'sql12392243',username ='sql12392243',password = 'aaditya@786a')
    
    cursor = connection.cursor()

=======
    connection = mysql.connector.connect(host='sql12.freesqldatabase.com',database='sql12392243',user='sql12392243',password='aaditya@786a')
    
    cursor = connection.cursor()
     
>>>>>>> Stashed changes
    cursor.execute("SELECT Name,Password FROM UserInfo")

    #Data to Tuple
    rows = cursor.fetchall()

    file = open('Account.csv', 'w', newline ='') 
  
    #writing the data into the file 
    with file:     
        write = csv.writer(file) 
        write.writerows(rows)

    
    
    def login(name1, password1):
        global success
        success = False
        file = open('Account.csv', 'rt')
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            if(a == name1 and b == password1):
                print("Welcome", a)
                success = True                
                break
            
    login(name,password)
    file.close()
    os.remove("Account.csv")
    
    if(success == True):
        print("Login Successfull!!!")
        os.system('python Start.py')
    else:
        print("Username or the password is invalid!!!")
        os.system('python Login.py')

def RegisterEnter(ID, NAME, HighScore, Tag):
    connection = mysql.connector.connect(host='sql12.freesqldatabase.com',database='sql12392243',user='sql12392243',password='aaditya@786a')
    
    myCursor = connection.cursor()

    sql = "INSERT INTO UserInfo(Name,Password,TotalScore,Tag) VALUES(%s,%s,%s,%s)"
    
    recordTuple = (ID,NAME,HighScore, Tag)
    
    myCursor.execute(sql, recordTuple)
    
    print("Registered Succesfully")
    
    
    connection.commit()
    connection.close()

    os.system('python Start.py')

def Register():

    global l

    connection = mysql.connector.connect(host = 'sql12.freesqldatabase.com',database = 'sql12392243',username ='sql12392243',password = 'aaditya@786a')
    
    cursor = connection.cursor()

    cursor.execute("SELECT Name FROM UserInfo")

    #Data to Tuple
    rows = cursor.fetchall()

    file = open('Account.csv', 'w', newline ='') 
  
    # writing the data into the file 
    with file:     
        write = csv.writer(file) 
        write.writerows(rows)
    
    print("Connection established")
    
    name = input('Enter your Username: ')

    #Checking If Username Is Correct
    with open('Account.csv', 'rt') as f:
             reader = csv.reader(f, delimiter=',')
             for row in reader:
                  if name == row[0]:
                       print('Username has already been taken')
                       l = True
                       os.system('python Start.py')
                       os.system('python Login.py')
                  else:
                      password = input('Enter your Password: ')
                      RegisterEnter(name,password, 0,'Newbie')
    f.close()                   
    os.remove("Account.csv")

def access(option):

     if(option == 'login'):
         print('\n')
         name = input("Enter your name: ")
         print("\n")
         password = input("Enter your password: ")
         Login(name,password)
     else:
        Register()

def begin():
    
    global option
    print("\n")
    print("Welcome To The Login Page")
    option = input("Login or Register(login, register): ")
    if(option!= "login" and option!= "register"):
        begin()

connect()
