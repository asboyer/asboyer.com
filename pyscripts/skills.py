import os
import json

files = os.listdir('../data/about/services/txt')

services = {}
i = 0

for file in files:
    f = open(f'../data/about/services/txt/{file}')
    lines = f.readlines()
    title = lines[0].strip('\n')
    body = lines[1:len(lines) - 1]
    img = lines[len(lines) - 1].strip('\n')

    body_string = ""
    for b in body:
        body_string += " " + b.strip('\n') + " "

    services[title] = {}
    services[title]['title'] = title
    services[title]['body'] = body_string.strip().replace("  ", " ").replace("  ", " ")
    services[title]['img'] = img
    services[title]['order'] = i

    i += 1

with open('../data/about/services/services.json', 'w') as json_file:
    json.dump(services, json_file, indent=4)