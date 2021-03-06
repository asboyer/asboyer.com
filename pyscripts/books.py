import json
from datetime import datetime
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
    for l in range(0, len(lines), 6):
        books.append([lines[l].strip(), lines[l+1].strip(), lines[l+2].strip(), lines[l+3].strip(), lines[l+4].strip(), lines[l+5].strip()] )

    for book in books:
        data[book[0]] = {
            "title": book[0],
            "author": book[1],
            "img": book[2],
            "link": book[3],
            "color": book[4],
            "year": int(book[5])
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

    for book in list(data):
        if data[book]['status'] == 'done':
            del data[book]['status']
            data[book]['year'] = datetime.now().year
            data[book]['stars'] = int(input(f'How many stars would you rate {data[book]["title"]}: '))
            with open(f'./data/favorites/books/list.json', 'r') as json_file:  
                book_list = json.load(json_file)
                book_list[book] = data[book]
            with open(f'./data/favorites/books/list.json', 'w') as json_file:
                json.dump(book_list, json_file, indent=4)
            if data[book]['stars'] == 5:
                del data[book]['stars']
                del data[book]['year']
                with open(f'./data/favorites/books/library.json', 'r') as json_file:
                    library = json.load(json_file)
                    library[book] = data[book]
                with open(f'./data/favorites/books/library.json', 'w') as json_file:
                    json.dump(library, json_file, indent=4)
            del data[book]            

    books = []
    for l in range(0, len(lines), 6):
        books.append([lines[l].strip(), lines[l+1].strip(), lines[l+2].strip(), lines[l+3].strip(), lines[l+4].strip(), lines[l+5].strip()])

    for book in books:
        data[book[0]] = {
            "title": book[0],
            "author": book[1],
            "img": book[2],
            "link": book[3],
            "color": book[4],
            "status": book[5]
        }

    with open(f'./data/favorites/books/shelf.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)