def main():
    fraction = input('Enter the gas level: ')
    percentage = convert(fraction)
    print(gauge(percentage))
    
    
def convert(fraction):
    try:
        fraction = fraction.split('/')
        a,c = fraction
        div = int(a)/int(c)
        perc = int(div*100)
        return perc
    except ZeroDivisionError:
        return 'Division by zero Error!'
    except ValueError:
        return 'Invalid input'

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <=1:
        return 'E'
    else:
        return str(percentage) + '%'
'''
def fuel(inp):
    try:
        inp = inp.split('/')
        a,c = inp
        div = int(a)/int(c)
        perc = int(div*100)
        if perc >= 99:
            return 'F'
        elif perc <=1:
            return 'E'
        else:
            return str(perc) + '%'
    except ZeroDivisionError:
        return "Error due to zero division"
    except ValueError:
        return "Invalid input"
'''
if __name__ == "__main__":
    main()  