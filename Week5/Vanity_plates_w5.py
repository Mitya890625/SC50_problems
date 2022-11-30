def main():
    str_plate = input('Plate: ')
    if is_valid(str_plate):
        print ('Valid')
    else: 
        print ('Invalid')
    

def is_valid(str):
    if str[0:2].isalpha() and 2<=len(str)<=6 and str[-2:].isdigit() and str[-2]!='0' and str[:].isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()  