d0 = {
    0: "Zero",
    1: "Uno",
    2: "Dos",
    3: "Tres",
    4: "Quatro",
    5: "Cinco",
    6: "Roku",
    7: "Nana",
    8: "Hachi",
    9: "Kyu",
    10: "Jyu",
}

d1 = {
    9: "Nine",
    11: "Eleven",
    3: "Three",
}

d0.update(d1)
for key, value in d0.items():
    print(key, value, sep=" -> ")

print()

l0 = [
    (12, "Jyuni"),
    (3, "Tres"),
    (0, "Shunya"),
]

d0.update(l0)
for key, value in d0.items():
    print(key, value, sep=" -> ")
