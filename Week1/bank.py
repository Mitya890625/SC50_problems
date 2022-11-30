def main():

    greetings = input("Greeting:")
    greetings = greetings.strip().lower().split()
    first_letter = list(greetings[0])
    print(greetings)
    print(first_letter)
    if greetings[0] == "hello":
        print("0$")
    elif first_letter[0] == 'h':
        print("20$")
    else:
        print("100$")

main()