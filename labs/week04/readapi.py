# Lab writing code to interact with an API.
# Author: Tom Brophy

import requests
import json

url = 'http://andrewbeatty1.pythonanywhere.com/books'

def read_books():
    response = requests.get(url)
    return response.json()

def read_book(id):
    get_url = url+'/'+str(id)
    response = requests.get(get_url)
    return response.json()

def create_book(book):
    response = requests.post(url, json=book)
    return response.json()

def update_book(id, book):
    put_url = url+'/'+str(id)
    response = requests.put(put_url, json=book)
    return response.json()

def delete_book(id):
    delete_url = url+'/'+str(id)
    response = requests.delete(delete_url)
    return response.json()

#book = {'Author': 'Terry Pratchett', 'Price': 7821, 'Title': 'The Colour of Magic'}
book = {'Title':'The Light Fantastic'}

if __name__ == '__main__':
    #print(read_book(510))
    #print(create_book(book))
    #print(update_book(538, book))
    print(delete_book(538))