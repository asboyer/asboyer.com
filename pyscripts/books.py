import json
def add_library():
    with open(f'./data/favorites/books/library.json', 'r') as json_file:  
        data = json.load(json_file)
    with open('./data/add/library.txt', 'r') as f:
        lines = f.readlines()
    f = open('./data/add/library.txt', 'w+')
    f.close()
    books = []
    for l in range(0, len(lines), 5):
        books.append([lines[l].strip(), lines[l+1].strip(), lines[l+2].strip(), lines[l+3].strip(), lines[l+4].strip()] )

    for book in books:
        data[book[0]] = {
            "title": book[0],
            "author": book[1],
            "img": book[2],
            "link": book[3],
            "color": book[4]
        }

    with open(f'./data/favorites/books/library.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def add_list():
    with open(f'./data/favorites/books/list.json', 'r') as json_file:  
        data = json.load(json_file)
    with open('./data/add/list.txt', 'r') as f:
        lines = f.readlines()
    f = open('./data/add/list.txt', 'w+')
    f.close()
    books = []
    for l in range(0, len(lines), 5):
        books.append([lines[l].strip(), lines[l+1].strip(), lines[l+2].strip(), lines[l+3].strip(), lines[l+4].strip()] )

    for book in books:
        data[book[0]] = {
            "title": book[0],
            "author": book[1],
            "img": book[2],
            "link": book[3],
            "color": book[4]
        }

    with open(f'./data/favorites/books/list.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def add_shelf():
    with open(f'./data/favorites/books/shelf.json', 'r') as json_file:  
        data = json.load(json_file)
    with open('./data/add/shelf.txt', 'r') as f:
        lines = f.readlines()
    f = open('./data/add/shelf.txt', 'w+')
    f.close()
    books = []
    for l in range(0, len(lines), 5):
        books.append([lines[l].strip(), lines[l+1].strip(), lines[l+2].strip(), lines[l+3].strip(), lines[l+4].strip()] )

    for book in books:
        data[book[0]] = {
            "title": book[0],
            "author": book[1],
            "img": book[2],
            "link": book[3],
            "color": book[4]
        }

    with open(f'./data/favorites/books/shelf.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)