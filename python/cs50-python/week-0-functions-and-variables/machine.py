# This program demonstrates global and local scope. It highlights the use of
# the `global` keyword to modify a global variable inside a function

# Avoid the use of global variables that have a high likelihood of being
# modified thorughout a program. Use capitalized snake case to signal that
# a variable is a constant (e.g. MAX_USERS = 100)
emoticon = "v.v"


def main():
    # The global keyword allows you to modify a global variable's value
    # inside a function, rather than creating a new local variable
    global emoticon
    say("test")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
