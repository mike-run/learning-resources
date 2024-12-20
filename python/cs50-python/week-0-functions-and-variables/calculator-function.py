def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    # These are equivalent ways of getting the square of a number
    #return n * n
    #return n ** 2
    return pow(n, 2)


main()