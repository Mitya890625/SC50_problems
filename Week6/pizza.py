import sys, csv
from tabulate import tabulate
try:
    if  len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif 'csv' not in sys.argv[1]:
        sys.exit("Not a csv file")
    else:
        pizzas = []

        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for type, small, large in reader:
                pizzas.append({"type": type, "small": small, "large": large})
        print(tabulate(pizzas,headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    print('File does not exist')
#for pizza in pizzas:
    #print(f"{pizza['type']};{pizza['small']};{pizza['large']}")"""