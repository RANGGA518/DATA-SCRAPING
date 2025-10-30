# from bs4 import BeautifulSoup
# import fungsi
# import requests

# def main_scraper(url, directory):
#     fungsi.create_directory(directory)
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     articles = soup.find_all(True, {"class" : "col-bs9-3"})

#     for article in articles:
#         article_format = "URL : " + article.a.get("href") + "\n"
        
#         if fungsi.does_file_exist(directory + "/artikel.txt") is False:
#             fungsi.create_new_file(directory + "/artikel.txt")
        
#         fungsi.write_to_file(directory + "/artikel.txt", article_format)
#         fungsi.get_details(article.a.get("href"))
#         print(article_format)

# fungsi.remove_file("hasil/articles.txt")
# main_scraper("https://tekno.kompas.com/read/2025/10/29/18580047/menggenggam-realme-15t-5g-hp-tipis-baterai-besar-yang-ringan-di-tangan","articles.txt")



from bs4 import BeautifulSoup
import fungsi
import requests
import os

def main_scraper(url, directory, filename):
    fungsi.create_directory(directory)
    print("Folder sudah dibuat:", directory)

    filepath = f"{directory}/{filename}"
    print("File output:", filepath)

    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, "html.parser")

    articles = soup.find_all(True, {"class": "article__list__title"})
    print("Jumlah artikel ditemukan:", len(articles))

    for article in articles:
        link_tag = article.find("a")
        if not link_tag:
            continue

        article_format = "URL : " + link_tag.get("href") + "\n"

        if not fungsi.does_file_exist(filepath):
            fungsi.create_new_file(filepath)

        fungsi.write_to_file(filepath, article_format)
        print("Tulis:", article_format)

    print("Selesai scraping.")

fungsi.remove_file("hasil/articles.txt")
main_scraper(
    "https://tekno.kompas.com/read/2025/10/29/18580047/menggenggam-realme-15t-5g-hp-tipis-baterai-besar-yang-ringan-di-tangan",
    "hasil",
    "articles.txt"
)
