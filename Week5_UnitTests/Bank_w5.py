def main():
    bank('Hello')




def bank(greet):
    greet = greet.strip().lower().split()
    first_letter = list(greet[0])
    if greet[0] == "hello":
        return '0$'
    elif first_letter[0] == 'h':
        return '20$'
    else:
        return '100$'

if __name__ == "__main__":
    main()  