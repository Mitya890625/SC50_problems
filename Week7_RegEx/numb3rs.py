import re, sys

def main():
    if validate(input("IPv4 address: ")):
        print("Valid")
    else:
        print("Invalid")


def validate(ip):
    matches = re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.){3}(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)$", ip)
    return matches


if __name__ == "__main__":
    main()