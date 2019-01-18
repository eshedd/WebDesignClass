import json

variable = "This is a value"
numVal = 12

if numVal is 12: 
    variable = "We hit our conditional"
        
    print(variable)

if numVal is 4:
    print("Imposible!")

def my_method():
    print("I invoked the my_method method. Are you not amused?!")

my_method()

my_array = ["First Element", "Second", 3, 4, 5]

for element in my_array:
    print(element)

data = ""
filename = "test.json"
with open(filename) as data_file:
    data = json.load(data_file)

for key in data: 
    print(key + " " + data[key])