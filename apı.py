list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
unique_to_first = set(list1) - set(list2)
tümü = set(list1) | set(list2)
print(common)
print(tümü)
print(unique_to_first )



users = ({"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25})
name_age_map = {user["name"]: user["age"] for user in users}
print(name_age_map)