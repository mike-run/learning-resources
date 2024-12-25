# This was created by ChatGPT so that water.py has something that it can use to
# work (this module was not provided by the lecturer for some reason)

import random

# Initialize global soil moisture
moisture_level = 50  # Starting moisture level

def sample():
    """
    Simulate sampling the soil's moisture level.
    The soil dries randomly by 1-10% each time this is called.
    """
    global moisture_level
    moisture_level -= random.randint(1, 10)
    if moisture_level < 0:
        moisture_level = 0  # Prevent negative moisture
    return moisture_level