animals = {
    "lion": ["King", "ferocious"],
    "leopard": ["stripes", "quick"],
    "snake": ["venomous", "slithers", "slim"],
    "frog": ["slimy", "poisonous"],
}

# Returns a shallow copy of the object
# things = animals.copy() # Although a separate copy of dictionary is created, underlying mutable list objects are the same.

# Use deepcopy function from the copy module to avoid this problem.
# from copy import deepcopy
# things = deepcopy(animals)

# Challenge: create a function like deepcopy() from copy module
def deepcopy_replica_at_one_level_depth(data: dict) -> dict:
    copy_dict = {}
    for key, value in data.items():
        copy_dict[key] = value.copy()
    return copy_dict

things = deepcopy_replica_at_one_level_depth(animals)

print(id(animals["frog"]), animals["frog"])
print(id(things["frog"]), things["frog"])
print()

things["frog"].append("amphibious")
print(animals["frog"])
print(things["frog"])
