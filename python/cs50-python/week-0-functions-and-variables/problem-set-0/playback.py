# This program prompts the user for input and then outputs that same input,
# replacing each space with `...` (i.e., three periods)

def main():
    user_input = input().replace(" ", "...")
    print(user_input)


main()