

# go to git bash
# git config --global user.name "Ruhee shah"
# git config --global user.email "ruheeshah8gamil.com"

# git init => initialize git
# git status => if you want to check what are the change
# git diff => if you want to check what are the changes
# git add .
# git commit -m "your message"
# copy paste git code from github

import requests 
from bs4 import BeautifulSoup
import json






url = "http://books.toscrape.com/" 


def scrape_book(url):
    response = requests.get(url)

    # Set encoding explicity to handle special characters correctly
    response.encoding = response.apparent_encoding

    if response.status_code !=200:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    book_list = []

    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        
        book_list.append({"title":title, "price":price, "currency":currency})
    with open("book.json","w",encoding="utf-8") as f:
        json.dump(book_list, f, indent=2,ensure_ascii=False)    
    
scrape_book(url)
