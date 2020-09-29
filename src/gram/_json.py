import json

arr = {
    'name': 'igsnow',
    'age': 10
}

jsonstr = json.dumps(arr)

print(arr, type(arr))
print(jsonstr, type(jsonstr))
