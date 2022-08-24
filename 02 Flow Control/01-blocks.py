name = input("Enter your name: ")
age = int(input("Enter you age: "))
print(name,age)

if age < 18:
    print("Please come back in {} years".format(18 - age))
elif age > 150:
    print("Voting is only for humans, {}. Sorry.".format(name))
    print("Live long and prosper though.")
else:
    print("You're old enough to vote. Long live democracy.")
