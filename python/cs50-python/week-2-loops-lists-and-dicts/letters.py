# This program generates personalized invitation letters by iterating through
# a list of Nintendo character names

def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

    # Alternate way of doing the same thing as for loop above using indexing
    # for i in range(len(names)):
    #     print(write_letter(names[i], "Princess Peach"))


def write_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {reciever},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()