import requests
from bs4 import BeautifulSoup
import os
import time

url = "https://www.goodreads.com/quotes/tag/{}"


print(" Love_Quotes          Inspirational_Quotes    Humor_Quotes            Philosophy_Quotes") 
print(" Life_Quotes          God_Quotes              Inspirational_Quotes    Truth_Quotes ")
print(" Wisdom_Quotes        Romance_Quotes          Poetry_Quotes           Death_Quotes ")
print(" Happiness_Quotes     Hope_Quotes             Faith_Quotes            Inspiration_Quotes ") 
print(" Writing_Quotes       Religion_Quotes         Life_Lessons_Quotes     Success_Quotes ")
print(" Motivational_Quotes  Relationships_Quotes    Time_Quotes             Knowledge_Quotes") 
print(" Love_Quotes          Spirituality_Quotes     Science_Quotes          Life_Quotes ")

qu = input("\n\nWhich type of quote would you like to read: ")

url = "https://www.goodreads.com/quotes/tag/" + qu


res = requests.get(url)
soup = BeautifulSoup(res.text, features="html.parser")
links = soup.find_all("a")

quote_divs = soup.find_all("div", attrs={"class" : "quote"})

i = 0

ch = 'y'

while (ch == 'Y' or ch == 'y'):
    os.system('cls')
    quote_div = quote_divs[i]
    quoteText_div = quote_div.find_next("div", attrs={"class" : "quoteText"})
    
    striped = quoteText_div.text.strip()
    striped_li = striped.split("\n")
    
    quote = striped_li[0][1:-1]
    author = striped_li[-1].strip()
    
    
    print("\n\nQuote: ", quote, "\n")
    print("Author: ", author)
    print("\n\n\n")

    ch = input("Want to view more quotes ?  Y/N: ")
    print("\n")

    i = i +  1
    
