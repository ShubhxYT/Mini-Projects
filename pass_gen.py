import random
import string

def generate_password(min_lenght,numbers=True,special_characters=True):
    letter = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits # 0123456789
    special = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    characters = letter

    if numbers:
        characters+=digits
    if special_characters:
        characters +=special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenth = int(input("Lenght of your password you want : "))
has_num = input("Do you want numbers in your password (Y/N) : ").lower() == 'y' # == 'y' will turn this into boolean true or false statement
has_special = input("Do you want speacial characters in your password (Y/N) : ").lower() == 'y'

pass_gen = int(input("How many passwords you would like to generate : "))
print(f"Here your generated passwords : ")
for i in range(pass_gen) :
    pwd = generate_password(min_lenth,has_num,has_special)
    print(f"{i+1} : {pwd}")
