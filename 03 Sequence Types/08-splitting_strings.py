panagram = """The quick brown 
fox jumps\tover
the lazy dog."""

words = panagram.split()    # Splits on blank-spaces by default
print(words)

number_str = "3,12,32,89,832,342,343,23,21"
number_str_list = number_str.split(",")
numbers = [int(num_str) for num_str in number_str_list]
print(numbers)
