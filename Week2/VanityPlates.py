def vanity_plates():
    while True:
        str = input("Plate: ")
        if str[0:2].isalpha() and 2<=len(str)<=6 and str[-2:].isdigit() and str[-2]!=0 and str[:].isalphanumeric():
            return True
        else:
            return False
        if str == 'q':
            break