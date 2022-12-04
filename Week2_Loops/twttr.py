def twttr(str):
    phrase = str
    dict1 = ['a','e','i','o','u']
    for i in phrase:
        if i in dict1:
            i = ''
            print(i, end='')
        else:
            print(i, end='')