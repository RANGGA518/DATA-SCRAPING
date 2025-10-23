from bs4 import BeautifulSoup

soup = BeautifulSoup('<html><body><div class="class1">'
'</div><div class="class2"></div><div class="class3"></div></body></html>')
soup.findAll(True, {"class":["class1", "class2"]})

# contoh multiclass
from bs4 import BeautifulSoup
import os
import fungsi
import requests

def main_scraper(url, directory):
    fungsi.create_directory(directory) 
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, 'html.parser')

    articles = soup.find_all("div", {'class': 'row article__wrap__grid--flex col-offset-fluid mt2'})
    articles2 = soup.find_all(True, {'class': ['article__grid']})

    for article in articles:
        print("URL : ", article.a.get("href"))
        print("Judul : ", article.text.strip())
        print()

    for article2 in articles2:
        print("URL2 : ", article2.a.get("href"))
        print("Judul2 : ", article2.text.strip())
        print()

main_scraper("https://tekno.kompas.com/gadget", "Hasil")

