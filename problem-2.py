'''
2) Write a new function with same functionality from Question 1, but it should be able to handle
a Python object in addition to a dictionary from Question 1.
'''

class Person(object):
    def __init__(self, first_name=None, last_name=None, father=None):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

def print_person(person, depth):
    print("first_name: ", depth)
    print("last_name: ", depth)
    print("father: ", depth)    
    if person.father:
      print_person(person.father, depth+1)
    
def print_depth(data, d=1):
    def find_depth(dictonary, depth):
        for key in dictonary.keys():
            print(key, depth)
            if isinstance(dictonary[key], dict):
                find_depth(dictonary[key], depth+1)
            if isinstance(dictonary[key], Person):
                print_person(dictonary[key], depth+1) 
  
    find_depth(data, d)

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
"key1": 1,
"key2": {
        "key3": 1,
    "key4": {
        "key5": 4,
        "User": person_b
    }}}

print_depth(a)