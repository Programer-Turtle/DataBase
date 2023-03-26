from cryptography.fernet import Fernet
import os
import time

def check_password():

    with open("passwordmanager\loginkey", "rb") as keysfile:
        key = keysfile.read()
        fernet = Fernet(key)

    with open("passwordmanager\password", "rb") as passwordsfile:
        password_encrypted = passwordsfile.read()
        password = fernet.decrypt(password_encrypted).decode()

    if input("Enter Password: ") == password:
        print("correct")
        # For Windows
        if os.name == 'nt':
           _ = os.system('cls')

        else:
            os.system('clear')
        return True
    
    else:
        print("Incorrect rerun program")
        time.sleep(2)
        return False