# This program prompts the user for the name of a variable in camel case and
# outputs the correspnding name in snake case. This program assumes that the
# input will be in camel case.

def main():
    camel_case = input("camelCase: ")
    snake_case = convert(camel_case)
    print(snake_case)


def convert(camel_case):
    snake_case = ""

    for character in camel_case:
        if character.isupper():
            snake_case += "_" + character.lower()
        else:
            snake_case += character

    return snake_case


main()