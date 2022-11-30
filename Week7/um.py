import re, sys

def main():
    print(count(input("Text: ")))
    
   


def count(s):
    count = 0
    list_of_ums = re.findall(r" um", s)
    for i in range(len(list_of_ums)):
        count +=1
    return count

    


if __name__ == "__main__":
    main()