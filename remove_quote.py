import json

num = int(input("Quote number: "))

with open(f'data/quotes/quotes.json', 'r') as json_file:
    data = json.load(json_file)

del data[str(num)]

if num != len(data.keys()):
    for i in range(num+1, len(data.keys()) + 1):
        print(f"{str(i)} -> {str(i-1)}")
        data[str(i-1)] = data[str(i)]
    del data[str(len(data.keys()) - 1)]

    new_dict = {}


    keys = []
    for key in data.keys():
        keys.append(int(key))
    keys.sort()
    for i in keys:
        new_dict[str(i)] = data[str(i)]

new_dict = data.copy()

with open(f'data/quotes/quotes.json', 'w+') as json_file:
    json.dump(new_dict, json_file, indent=4)