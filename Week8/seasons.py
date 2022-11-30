from datetime import date
import inflect, re, sys
#program that converts date in format YYYY-MM-DD to minutes
def main():

    birth_date = input("Date of birth: ")
    current_date = str(date.today())
    matches = re.search(r"^\d\d\d\d-(0\d|1[0-2])-(0\d|1\d|2\d|3[01])$", birth_date)
    if matches:
        time = time_in_minutes(birthdate_convert(birth_date), current_date_convert(current_date))
        print(type(time))
        print(convert_to_words(time) +" minutes")
    else:
        sys.exit("Invalid date")


    



def birthdate_convert(bd):
    year, month, day = bd.split("-")
    bd_min = 525600*int(year) + 43200*int(month) + 1440*int(day)
    return bd_min

def current_date_convert(cd):
    year_c, month_c, day_c = cd.split("-")
    cd_min = 525600*int(year_c) + 43200*int(month_c) + 1440*int(day_c)
    return cd_min
def time_in_minutes(bd, cd):
    return cd - bd
def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words



if __name__ == "__main__":
   main()