from passwordmanager.Login import *
from cryptography.fernet import Fernet
import os

skip_password = False

def checkcommand(command):
    if command == "cls" or "clear":
        if os.name() == "nt":
            os.system("cls")
        else:
            os.system("clear")

def main():
    while True:
        userchoice = input("DataBase>")
        checkcommand(userchoice)
        

if __name__ == "__main__":
    if not skip_password:
        if check_password():
            main()
        else:
            exit()

    else:
        main()