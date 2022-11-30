import re, sys

def main():
    print(parse(input("HTML: ")))
   


def parse(s):
    matches = re.search(r"https://www\.youtube\.com/embed/xvFZjo5PgG0", s) 
    pulled_str = matches.group()
    new_str = re.sub(r"www\.youtube\.com/embed", "youtu.be", pulled_str)
    return new_str


if __name__ == "__main__":
    main()