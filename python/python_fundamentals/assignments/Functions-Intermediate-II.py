
x = [ [5, 2, 3], [10, 8, 9] ]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
    ]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Q1,2 - :Part[1-4] Update Values in Dictionaries and Lists
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print("New Data \n", students, "\n", sports_directory, "\n", z)

print("\n---------------------------------------------------------------------------------------\n")


# Q3,4 - :Iterate Through a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for dict in some_list:
        output = [] # reusable pattern idea
        for key, value in dict.items():
            output.append(f"{key} - {value}") # string interpolition idea
        print(",  ".join(output)) # before going two next dict print what you have using join to insert the ,

iterateDictionary(students)

print("\n---------------------------------------------------------------------------------------\n")

# Q5,6 - : Get Values From a List of Dictionaries
def iterateDictionary2(name, some_list):
    for dict in some_list:
        if name in dict:
            print(dict[name])
    print("\n")

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print("\n---------------------------------------------------------------------------------------\n")

# Q7,8 - :Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        values = some_dict[key]
        print(f"{len(values)} {key.upper()}")
        for item in values:
            print(item)
        print("\n")

printInfo(dojo)

print("\n---------------------------------------------------------------------------------------\n")
