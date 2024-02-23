from readapi import read_books
import requests


books = read_books()

count = 0
total = 0

for book in books:
    count += 1
    total += book['Price']

print (f'The number of books is {count}, the total cost of the books is {total}, and the average price is {total/count}')