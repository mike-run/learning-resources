# This program demonstrates how to iterate over lists and dictionaries

# List of dictionaries
students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# # Dictionaries
# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }

# # With regards to students[student], the "students" is the name of the
# # dictionary. It tells Python "I want to look something up in the dictionary
# # named students". You give the key (student) and it gives the corresponding 
# # value
# for student in students:
#     print(student, students[student], sep=", ")

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# # Lists
# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])