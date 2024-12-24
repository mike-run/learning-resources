# This program prints various shapes using "#" and loops

def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(height):
    for _ in range(3):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("# ", end="")
        print()


# These two functions here are the equivalent to the function above
# def print_square(size):
#     for i in range(size):
#         print_row(size)


# def print_row(width):
#     print("#" * width)


main()