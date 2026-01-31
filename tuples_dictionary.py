#Creating dictionaries from tuples

grades = {
    ("John","Math"): 5,
    ("Alice","Science"): 4,
    ("Bob","History"): 3
}
john_math = grades[("John","Math")]
print("John's Math grade is:", john_math)

grades[("John","Science")] = 5
print("Alice's updated Science grade is:", grades[("Alice","Science")])

#Creating a list of dictionary keys
keys = list(grades.keys())

student,subject = keys[0]
print("First key - Student:", student, "Subject:", subject)