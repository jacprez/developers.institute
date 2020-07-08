states = [
    {
        "state":"New Jersey",
        "capital": "Trenton",
        "continent": "North America"
     },
    {
        "state":"New York",
        "capital": "Albany",
        "continent": "North America"
    },
    {
        "state":"Pennsylvania",
        "capital": "Harrisburg",
        "continent": "North America"
    },
    {
        "state":"Wisconsin",
        "capital": "Madison",
        "continent": "North America"
    }
]
print(states[-1]["capital"])


countries = [
	{
		'country': 'South Africa',
		'capital': 'Pretoria',
		'continent': 'Africa'
	},
	{
		'country': 'USA',
		'capital': 'Washington DC',
		'continent': 'North America'
	},
	{
		'country': 'Panama',
		'capital': 'Panama City',
		'continent': 'North America'
	},
	{
		'country': 'Israel',
		'capital': 'Jerusalem',
		'continent': 'Asia'
	},
	{
		'country': 'Palestine',
		'capital': 'Al Quds',
		'continent': 'Asia'
	}
]

number_of_continents = set()
for country in countries:
    number_of_continents.add((country["continent"]))

print(f"Number of continents is: {len(number_of_continents)}")



# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]
for key in keysToRemove:
    del sampleDict[key]
print(sampleDict)



# Hashtable
names = ["jon", "jackie", "gabi", "dennis", "kobe"]
phonebook = {}
for name in names:
    key = name[0].upper()
    if key not in phonebook:
        phonebook[key] = [name]
    else:
        phonebook[key].append(name)
print(phonebook)

# letter_lookup = {name[0].upper() : name for name in names}
# print(letter_lookup)