# This program is a tip calculator and calulates the tip needed given how much
# a meal was (in dollars) and a percent provided by the user


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    convert_to_float = float(d.strip("$"))
    return convert_to_float


def percent_to_float(p):
    convert_to_percent = float(p.strip("%")) / 100
    return convert_to_percent


main()