import requests
import fungsi
from bs4 import BeautifulSoup

result = requests.get("https://www.Detik.com/")
print(result)
print(result.encoding)
print(result.status_code)
print(result.elapsed)
print(result.url)
print(result.history)
print(result.headers["Content-Type"])

# # LOGIC
def main_scraper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    print(soup.find_all("div", {"class" : "grid-row list-content list-content--column"}))
    
main_scraper("https://www.detik.com/", "Hasil")






