def main():
    expression = input("Enter expression please:")
    x,y,z = expression.split(" ")    
    if y == '+':
        print(float(x)+float(z))
    elif y == '-':
        print(float(x)-float(z))
    elif y == '*':
        print(float(x)*float(z))
    elif y == '/':
        if z == '0':
            print("Division by zero!")
        else:
            print(float(x)/float(z))
main()