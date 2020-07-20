dic2 = {}
def print_depth(data,depth=0):
    for key, value in data.items():
        dic2[key] = depth+1
        if isinstance(value, dict):
            print_depth(value, depth=depth+1)
       
data = {
    "key1":1,
    "key2": {
        "key3":1,
        "key4": {
            "key5":4
        }
    }
}
print_depth(data)
arr1 = sorted(dic2.items(),key=lambda x: x[0])
for key,val in arr1:
    print(" ".join([str(key),str(val)]))