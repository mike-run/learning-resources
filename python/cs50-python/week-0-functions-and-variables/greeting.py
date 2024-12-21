# This program checks to see if "hello" is in the user's input and prints
# a different greeting based on if the string is present or not

def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"


greeting = greet("hello, computer")
print(greeting)

greeting = greet("hi, how's the weather?")
print(greeting)