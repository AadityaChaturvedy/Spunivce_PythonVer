import mysql.connector
import os

def DeleteAccount():
    connection = mysql.connector.connect(host = 'sql12.freesqldatabase.com',database = 'sql12392243',username ='sql12392243',password = 'aaditya@786a')
    
    cursor = connection.cursor()

    a = input('Enter your password: ')

    recordTuple = (a)

    sql = """Delete from UserInfo where Password = %s"""   

    cursor.execute(sql, (recordTuple,))
    connection.commit()
    connection.close()

    while True:
        print('Account Deleted')
        os.system('python Start.py')
        break
    else:
        print('Unsucessful')

DeleteAccount()

