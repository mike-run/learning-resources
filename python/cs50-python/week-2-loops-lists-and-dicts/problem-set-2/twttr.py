# This program prompts the user for a str of text and then outputs that same
# with the vowels (A, E, I, O, U) removed

def main():
    text = input("Input: ")

    for character in text:
        if character not in "aeiouAEIOU":
            print(character, end="")
    print()

main()