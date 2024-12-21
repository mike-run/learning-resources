# This program implements a function called convert that accepts a str as input
# and returns that input with any `:)` or `:(` converted to the equivalent
# emoji


def main():
    user_input = input("Please enter a string with a happy ':)' and/or sad ':(' emoji: ")
    print(convert(user_input))


def convert(str):
    new_str = str.replace(":)", "🙂").replace(":(", "🙁")
    return new_str


main()