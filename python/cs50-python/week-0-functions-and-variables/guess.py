# This program prompts the user for a number and then tells them whether they
# correctly guessed the right number, which is 50

def get_guess():
    guess = int(input("Please guess a number: "))
    return guess


def main():
    guess = get_guess()

    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


main()