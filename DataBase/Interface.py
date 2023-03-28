import passwordmanager.Login as login
from cryptography.fernet import Fernet
import os

print(os.getcwd())

skip_password = False

def checkcommand(command):
    #clears terminal
    if command == "cls" or command == "clear":
        os.system("cls")
    
    #Uses command prompt
    elif command[0:4] == "cmd>":
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

    else:
        print("User_Error. This is not a command!")
       

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