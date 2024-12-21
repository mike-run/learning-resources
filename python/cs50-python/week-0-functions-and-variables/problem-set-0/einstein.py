# This program prompts the user for mass as an integer (in kilograms) and then
# outputs the equivalent number of Joules as an integer


def main():
    mass = int(input("m: "))
    joules = mass * (300000000 ** 2)
    print(joules)


main()