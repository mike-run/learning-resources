# This program demonstrates how to manipulate lists using different methods

results = [
    "Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", 
    "Bowser", "Donkey Kong Jr."
]

results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse()

# results = ["Mario", "Luigi"]

# results.append("Princess")
# results.append("Yoshi")
# results.append("Koopa Troopa")
# results.append("Toad")

# results.append(["Bowser", "Donkey Kong Jr."])
# results.remove(["Bowser", "Donkey Kong Jr."])
# results.extend(["Bowser", "Donkey Kong Jr."])

print(results)