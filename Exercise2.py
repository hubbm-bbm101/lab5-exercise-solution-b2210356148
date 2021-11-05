mail = input("Write your email: ")
def checkMail(mail):
 if "@" and "." in mail:
    print("You entered valid mail adress: "+mail)
 else:
    print("You have not entered '@' or '.' Please check your mail adress.")
print(checkMail(mail))