import sys,csv, tabulate
try:
    if  len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif 'csv' not in sys.argv[1]:
        sys.exit("Not a csv file")
    else:
        students = []

        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
            for student in students:
               last_name, first_name = student['name'].split(',')
               first_name = first_name.lstrip() 
               students.append({"first": first_name, "last": last_name, "house": student['house']})
            print(tabulate(students,headers="firstrow", tablefmt="grid"))
            """
            for student in students:
                last_name, first_name = student['name'].split(',')
                first_name = first_name.lstrip()
                print(f"{first_name} {last_name} is from {student['house']}")
        with open(sys.argv[2], "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                last_name, first_name = student['name'].split(',')
                first_name = first_name.lstrip()
                writer.writerow({"first": first_name, "last": last_name, "house": student['house']})"""       
except FileNotFoundError:
    print('File does not exist')