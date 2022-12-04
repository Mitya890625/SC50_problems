import re, sys, validators

def main():
    if validate(input("Enter your email: ")):
        print("Valid")
    else:
        print("Invalid")
    
   


def validate(s):
    return validators.email(s)
    

    


if __name__ == "__main__":
    main()