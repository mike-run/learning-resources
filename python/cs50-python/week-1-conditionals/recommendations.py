# This program suggests a game depending on the difficulty and number of
# players the user inputs


def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            recommend("Please enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Please enter a valid number of players")
    else:
        print("Please enter a valid difficulty")


def recommend(game):
    print("You might like", game)


main()