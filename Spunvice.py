import os

print('\n'"Hello user welcome to the app. This app is made by Aaditya Chatuvrvedy and Divyansh Manas.")

def Info():
        print('\n')
        print("Type 'GLI' To Start, type 'CHL' for Changelogs or type 'INFO' for info related to games and utilities in this app:- ")
        z=input()

        if(z == "CHL"):
                file = open('Changelogs.txt', 'r')
                lines = file.readlines()
                print('\n')
                for line in lines:
                    print(line.strip())
            
                file.close()

                Info()
                
        elif(z == "GLI"):
                os.system('python Login.py')

        elif(z == "INFO"):
                file = open('Info.txt', 'r')
                lines = file.readlines()
                print('\n')
                for line in lines:
                    print(line.strip())
            
                file.close()
                Info()
                
        elif(z != "CHL" or z != "INFO" or z != "GLI"):
                Info()
        

Info()
input()
