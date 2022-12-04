def main():
    word = input()
    a = shorten(word)
    print(a)




def shorten(word):
    dict1 = ['a','e','i','o','u','A','E','I','O','U']
    x = ''
    for i in word:
        if i in dict1:
            i =''
            x += i
        else:
           x +=i
    return x


if __name__ == "__main__":
    main()   