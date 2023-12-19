import string
import random
import pyperclip
def generatePassword(length,wantUppers,wantLowers,wantNumbers,wantSymbols):
    theSet=""
    if(wantUppers):
        theSet=theSet+string.ascii_uppercase
    if(wantLowers):
        theSet=theSet+string.ascii_lowercase
    if(wantNumbers):
        theSet=theSet+string.digits
    if(wantSymbols):
        theSet=theSet+string.punctuation
    if not theSet:
        print("Choose atleast a single type of the chracter set or else the password cant be generate.")
        return None
    password="".join(random.choice(theSet) for _ in range(length))
    return password
def main():
    print("Command-Line Password Generator")
    length = int(input("Enter the desired password length: "))
    wantUppers = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    wantLowers = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    wantNumbers = input("Include numbers? (yes/no): ").lower() == "yes"
    wantSymbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generatePassword(length, wantUppers, wantLowers, wantNumbers, wantSymbols)
    if password:
        print(f"Generated password us {password}")
        wantToClickboard=input("Do you want to copy your password to the clickboard? (yes/no): ").lower()=="yes"
        if(wantToClickboard):
            pyperclip.copy(password)
            print("The password has been copied to your clickboard")
if __name__=="__main__":
    main()