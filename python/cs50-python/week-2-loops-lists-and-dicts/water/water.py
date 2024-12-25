from soil import sample


def main():
    # Gets an initial moisture reading so that the while loop further below has
    #  a value to check against
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")


if __name__ == "__main__":
    main()