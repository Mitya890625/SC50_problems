def main():

    greetings = input("Greeting:")
    greetings = greetings.strip().lower().split() #split input string and lower case of it
    first_letter = list(greetings[0]) #makes list from string
    print(greetings)
    print(first_letter)
    if greetings[0] == "hello": #checks if first word is "hello"
        print("0$")
    elif first_letter[0] == 'h': #checks if first letter is "h"
        print("20$")
    else:
        print("100$")

main()
"""
some changes that I want to test
"""
