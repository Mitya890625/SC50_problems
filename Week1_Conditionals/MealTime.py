def main():
    time = input("Enter the time:").split(':')
    hours, minutes = time
    time_converted = float(hours) + float(minutes)/60
    if time_converted <= 24:
        if 7 <= time_converted <=8:
            print("It's breakfast time!")
        elif 12 <= time_converted <=13:
            print("It's lunch time!")
        elif 18 <= time_converted <=19:
            print("It's dinner time!")
        else:
            print("It isn't time to eat!")
    else:
        print("invalid time!")
main()