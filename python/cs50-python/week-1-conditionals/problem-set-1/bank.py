# This program prompts the user for a greeting and outputs a certain cash
# prize depending on the user's greeting

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello") == True:
    print("$0")
elif greeting.startswith("h") == True:
    print("$20")
else:
    print("$100")