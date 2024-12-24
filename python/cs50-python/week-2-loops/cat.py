# This program demonstrates for and while loops in Python

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n # use break if not in a function to get out of loop

def meow(n):
    for _ in range(n):
        print("meow")


main()


# For loop
# for _ in range(3):
#     print("meow")

# for i in [0, 1, 2]:
#     print("meow")

# print("meow\n" * 3, end="")


# While loop 
# i = 0
# while i < 3:
#     print("meow")
#     i += 1 # i++ does not exist in Python