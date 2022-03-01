shopping_list = ['milk', 'cola', 'eggs', 'flour', 'chicken', 'noodles']
item_to_find = input('Enter item for your search: ').casefold()
found_at = None     # None tells that no value has been bound to found_at variable

# for i in range(len(shopping_list)):
#     if shopping_list[i] == item_to_find:
#         found_at = i
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at:
    print('{} is item {} in the shopping list'.format(item_to_find,found_at+1))
else:
    print(item_to_find,'not found in shopping list')
