def main():
    smile = input("Enter your emoji: ")
    convert(smile)


def convert(s):
    s = s.replace(':)', '🙂').replace(':(', '🙁')
    print(s)

main()