# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_sample = zip(keys,values)
print(dict(dict_sample))

# Exercise 2

store = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US" : ["pink", "green"]
        }
}
# 2. 
store["number_stores"] = 2 
print(store)
# 3
international_competitors = store["international_competitors"]
seperator = ", "

print(f"Zara's international competitors are : {seperator.join(international_competitors)}")
# 4
store["country_creation"] = "Spain"
print(store)
# 5
if "international_competitors" in store:
    store["international_competitors"].append("Desigual")
    print(store)
# 6
del store["creation_date"]
print(store)
# 7
print(international_competitors[-1])
# 8
major_colors_in_us = store["major_color"]["US"]
sep = " and "
print(f"The major clothes' colors in the United States are: {sep.join(major_colors_in_us)}")
# 9
print(len(store))
# 10
print(store.keys())
# 11
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000 
}
store.update(more_on_zara)
print(store)

# Exercise 3
# 1
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
indexes = []
for index, user in enumerate(users):
    indexes.append(index)

new_dict = dict(zip(users, indexes))
print(new_dict)
# 2 
newnew_dict = dict(zip(indexes, users))
print(newnew_dict)
# 3
sorted_users = sorted(tuple(users))
sorted_dict = dict(zip(sorted_users, indexes))
print(sorted_dict)
# index = 0
# while index < len(users):
#     print((index, users[index])
#     index += 1
