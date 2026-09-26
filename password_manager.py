import random
import string
passwords={}
try:
    with open ("passwords,txt","r") as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website]=pwd
except:
    pass
def generate_password():
    chars=string.ascii_letters+string.digits+"!@#$%&"
    password="".join(random.choice(chars)for i in range(8))
    return password
while True:
    print("\n----PERSONAL PASSWORD MANAGER----")
    print("1.save password")
    print("2.view password")
    print("3.generate password")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=="1":
        site=input("enter website:")
        pwd=input("enter password:")
        passwords[site]=pwd
        with open("passwords.txt","a")as file:
            file.write(f"{site}:{pwd}\n")
        print("Saved!")
    elif choice=="2":
        if not passwords:
            print("No data")
        else:
            for site,pwd in passwords.items():
                print(site,":",pwd)
    elif choice==3:
        print("generated password",generate_password)
    elif choice=="4":
        print("ok bye..")
        break
    else:
        print("Invalid input")
    





