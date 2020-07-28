'''
1) Write the following function’s body. A nested dictionary is passed as parameter. You need to
print all keys with their depth.
'''

def print_depth(data, d=1):
    def find_depth(dictonary, depth):
        for key in dictonary.keys():
            print(key, depth)
            if type(dictonary[key]) is type({}):
                find_depth(dictonary[key], depth+1)        
    find_depth(data, d)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}
    

print_depth(a)