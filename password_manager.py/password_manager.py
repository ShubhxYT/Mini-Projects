from cryptography.fernet import Fernet, InvalidToken #to encrypt our password

#========= Key generater for this code (need to be run once atleast to gen key) ============
def write_key():
    key = Fernet.generate_key()
    with open("D:/Codes/projects/password_manager.py/key.key","wb") as key_file:
        key_file.write(key)
#write_key()
#==========================================================================================

def decrypt_password(token): #function for checking if the token is invalid
    try:
        decrypted_pass = fer.decrypt(token.encode())
        return decrypted_pass.decode()
    except InvalidToken:
        return "Invalid Token"
    
def load_key():
    file = open("D:/Codes/projects/password_manager.py/key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() #generating a personal key for this program
fer = Fernet(key)

def view():
    with open("D:/Codes/projects/password_manager.py/password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            decrypted_pass = decrypt_password(pwd)
            decrypted_pass = fer.decrypt(pwd.encode())
            print("User:", user, "| Password:", decrypted_pass.decode())

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    encoded_pwd = fer.encrypt(pwd.encode()) # Encoding the password

    with open("D:/Codes/projects/password_manager.py/password.txt",'a') as f:
        f.write(name + "|" + encoded_pwd.decode() + "\n")


while True: 
    mode = input("Add new password or view existing one ? (view,add,'q' to quit) : ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
        continue
    elif mode == 'add':
        add()
        continue
    else:
        print("Invald Mode.")
        continue