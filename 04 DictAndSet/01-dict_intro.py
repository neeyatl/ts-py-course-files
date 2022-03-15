emperors = {
    'rome': "Augustus Caesar",
    'japan': "Hirohito",
    'maratha': "Shivaji Maharaj",
}

emperors['mourya'] = "Ashoka Mourya"
emperors['france'] = "Napoleon Bonaparte"

# Update rome
emperors["rome"] = "Markus Antonius"

# del emperors["japan"]         # Throws an error if key doesn't exist
emperor_of_japan = emperors.pop("japan")           # Throws an error if key doesn't exist 
italian_emperor = emperors.pop("italy", None)     # unless second argument, default value, is passed
print(emperor_of_japan)
print(italian_emperor,"\n")

# Less Efficient
# for key in emperors:
#     print(key, emperors[key], sep=" => ")

# More Efficient
for key, value in emperors.items(): # enumerate for sequences & .items() for dictionaries
    print(key, value, sep=" => ")