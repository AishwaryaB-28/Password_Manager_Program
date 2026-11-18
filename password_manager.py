import random
import string

password = {}

#load an existing password

try:
    with open("password.txt", "r")as file:
        for line in file:
            website, pwd = line.strip().split(":")
            password[website] = pwd

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. save password")
    print("2. view password")
    print("3. generate password")
    print("4. exit")

    #save password

    choice = input("enter your choice: ")

    if choice == "1":
        site = input("enter website: ")
        pwd = input("enter password: ")
        password[site] = pwd

        with open("passwords.txt", "a")as file:
            file.write(f"{site}:{pwd}\n")

        print("saved!")

    #view password

    elif choice == "2":
        if not password:
            print("no data")
        else:
            for site, pwd in password.items():
                print(site, ":", pwd) 

    #generate password

    elif choice =="3":
        print("Generated password", generate_password())

    #exit
    
    elif choice == "4":
        print("Ok bye..")
        break
    else:
        print("Invalid input")

                       
