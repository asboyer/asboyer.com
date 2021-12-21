import json
from datetime import date
def add_quote():
    with open(f'./data/quotes/quotes.json', 'r') as json_file:
        data = json.load(json_file)
        length = len(data)
    with open('./data/add/quotes.txt', 'r') as f:
        lines = f.readlines()
        quotes = []
        i = 0
        j = 0
        while i < len(lines):
            lines[i] = lines[i][0].upper() + lines[i][1:].strip()
            lines[i] = (lines[i] + ".").replace("..", ".")
            quotes.append([lines[i]])
            lines[i + 1] = lines[i + 1][0].upper() + lines[i + 1][1:]
            quotes[j].append(lines[i + 1].strip())
            j += 1
            i += 2
    f = open('./data/add/quotes.txt', 'w+')
    f.close()
    quote_dict = {}
    i = length
    for q in quotes:
        quote_dict[i] = {}
        quote_dict[i]['quote'] = q[0]
        quote_dict[i]['author'] = q[1]
        quote_dict[i]['date_added'] = date.today().strftime("%B %d, %Y")
        i += 1
    data.update(quote_dict)
    with open(f'./data/quotes/quotes.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)