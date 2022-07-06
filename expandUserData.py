import numpy as np
import pandas as pd

books = pd.read_csv('./Books.csv')

import requests

base_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

Pages = []
Category = []
Rating = []
RatingCount = []

for item in books['ISBN']:
    url =  base_url + item
    res = requests.get(url=url)
    data = res.json()
    
    if data['totalItems'] == 0:
        continue
        
    if 'volumeInfo' not in data['items'][0]:
        continue
        
    if 'pageCount' in data['items'][0]['volumeInfo']:
        Page.append(data['items'][0]['volumeInfo']['pageCount'])
    else:
        Page.append(None)
        
    if 'categories' in data['items'][0]['volumeInfo']:
        Category.append(data['items'][0]['volumeInfo']['categories'][0])
    else:
        Category.append(None)
        
    if 'averageRating' in data['items'][0]['volumeInfo']:
        Rating.append(data['items'][0]['volumeInfo']['averageRating'])
    else:
        Rating.append(None)
        
    if 'ratingsCount' in data['items'][0]['volumeInfo']:
        RatingCount.append(data['items'][0]['volumeInfo']['ratingsCount'])
    else:
        RatingCount.append(None)

import numpy as np

books['Price'] = np.random.uniform(10, 150, (books.shape[0]))
books['Pages'] = Pages
books['Category'] = Category
books['Rating'] = Rating
books['RatingCount'] = RatingCount


books.to_csv('books_expand.csv', index=False)