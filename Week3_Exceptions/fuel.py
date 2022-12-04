def fuel(inp):
    try:
        inp = inp.split('/')
        a,c = inp
        div = int(a)/int(c)
        perc = int(div*100)
        print(str(perc)+'%')
        if perc > 99:
            print('F')
        elif perc <1:
            print('E')         
    except ZeroDivisionError:
        print("Error due to zero division")
    except ValueError:
        print("Invalid input")