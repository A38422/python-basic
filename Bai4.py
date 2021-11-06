import requests

def find_dict(title, completed):
    link = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(link)
    arr = []
    for i in response.json():
        if title in i['title'] and completed == i['completed']:
            arr.append(i)
    return arr

print(find_dict("autem", False))