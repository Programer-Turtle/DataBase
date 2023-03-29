from cryptography.fernet import Fernet
import time
import os

#Test errormanager
try:
    from errormanager import *

except:
    print("Error manager dosn't exsist your system wont run redownload system from https://github.com/Programer-Turtle/DataBase")

#checks system stability
try:
    with open("passwordmanager\password"):
        None
        
    with open("passwordmanager\loginkey"):
        None

    import passwordmanager.Login as login
    
except:
    error("system", "Damaged Files Redownload system! https://github.com/Programer-Turtle/DataBase")
    time.sleep(3)
    

skip_password = False

def checkcommand(command):
    #clears terminal
    if command == "cls" or command == "clear":
        os.system("cls")
    
    #Uses command prompt
    elif command.startswith("cmd>"):
        os.system(command[4:len(command)])

    #Creates new file
    elif command.startswith("newfile>"):
        for value, letters in enumerate(command[8:], start=8):
            file_path = os.path.join("User_files", command[8:value])
            if letters == ":":
                x = open(file_path, "w")
                x.write(command[value+1: len(command)])
                x.close()
                return
            
        #If no text to add
        file_path = os.path.join("User_files", command[8:len(command)])
        x = open(file_path, "w")
        x.close()

    elif command.startswith("deletefile>"):
        file_path = os.path.join("User_files", command[11:len(command)])
        try:
            os.remove(file_path)
        except:
            error("user", "FileNotFound!")

    elif command.startswith("readfile>"):
        file_path = os.path.join("User_files", command[9:len(command)])
        try:
            with open(file_path, "r") as file_data:
                print(file_data.read())
        except:
            error("user", "FileNotFound!")

        

    else:
        error("user", "This is not a command!")
       

def main():
    while True:
        userchoice = input("DataBase>")
        checkcommand(userchoice)
        

if __name__ == "__main__":
    if not skip_password:
        if login.check_password():
            main()
        else:
            exit()

    else:
        main()