with open("day2.inp", "r") as f:
    items = f.read()
    
items = items.split("\n")
items = list(map(lambda i: i.split(" "), items))

"""
part 1

points = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3,
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9,
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6,
    },
}
"""
points = {
    "A": {
        "Y": 4,
        "Z": 8,
        "X": 3,
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9,
    },
    "C": {
        "Z": 7,
        "X": 2,
        "Y": 6,
    },
}

items = list(filter(lambda i: len(i) == 2, items))
items = [points[i[0]][i[1]] for i in items]
print(sum(items))