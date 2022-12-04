def main():
    m = int(input("Enter the mass: "))
    calculate(m)

def calculate(mass):
    E = mass * 3000000**2
    print(E)

main()