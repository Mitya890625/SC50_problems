import sys
try:
    if  len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif 'py' not in sys.argv[1]:
       sys.exit("Not a Python file") 
    else:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            count=0
            for line in lines:
                if line.isspace() or line.startswith('#'):
                    pass
                else:
                    count +=1 
        print(count)
except FileNotFoundError:
    print("File does'nt exist")