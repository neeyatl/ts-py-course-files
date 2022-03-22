from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # union creates and returns a new set
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction

#     # update is more efficient as new set isn't created and returned
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction

# making the above code even more efficient
meds_to_watch.update(*adverse_interactions)

print(*sorted(meds_to_watch), sep="\n")


marvel = {'Captain America', 'Hawkeye', 'Black Widow', 'Valkyrie', 'Thor'}
dc = {'Wonder Woman', 'Batman', 'Mera', 'Superman'}

# comics_superheroes = marvel.union(dc)
comics_superheroes = marvel | dc
print()
print(comics_superheroes)
