def main():

    question = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    validator(question)


def validator(q):
    if q == "42":
        print("Yes")
    elif q == "forty-two":
        print("Yes")
    elif q == "forty two":
        print("Yes")
    else:
        print("No")
    
main()