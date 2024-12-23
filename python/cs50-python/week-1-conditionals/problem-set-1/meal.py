# This program prompts the user for a time and outputs whether it's breakfast
# time, lunch time, or dinner time. If it's not time for a meal, it outputs
# nothing (this program assumes that the users input will be formatted in 
# 24-hour time)


def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    time = int(hours) + minutes
    return float(time)


if __name__ == "__main__":
    main()