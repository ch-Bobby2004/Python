# numbers can be dictionary keys in Python because they are immutable
data = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(data[1])

marks = {
    1.1: "Math",
    2.2: "Science"
}

print(marks[1.1])

for key, value in marks.items():
    print(key , ": " ,value)