class Person:
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
 
 
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
 
data = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b
        }
    }
}
 
ans = []
 
 
def class_depth(klass, depth):
    tmp = {'first_name:': depth}
    ans.append(tmp)
    tmp = {'last_name:': depth}
    ans.append(tmp)
    tmp = {'father:': depth}
    ans.append(tmp)
    if isinstance(klass.father, Person):
        # print('aaaa')
        class_depth(klass.father, depth + 1)
 
 
def print_depth(data, depth=0):
    for key, value in data.items():
        tmp = {
            key: depth+1
        }
        ans.append(tmp)
        if isinstance(value, dict):
            print_depth(value, depth=depth + 1)
        if isinstance(value, Person):
            depth += 1
            class_depth(value, depth + 1)
 
 
print_depth(data)
lis = []
for i in ans:
    lis.append(i.items()[0])
 
arr2 =sorted(lis,key=lambda x: x[1])
 
for i in arr2:
    print(" ".join([str(i[0]),str(i[1])]))