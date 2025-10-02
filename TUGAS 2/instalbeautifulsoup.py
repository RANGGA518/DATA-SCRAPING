from bs4 import BeautifulSoup
import os

html1 = "<p>This is a Div</p>"
soup = BeautifulSoup(html1, "html.parser")
print(soup.p.text)

html = "<div>Ini adalah dokumen div</div><p>Ini adalah paragraf halaman</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.p.text)

html = """<div>ini div</div><p>ini paragraf</p><div>p</div>"""
soup = BeautifulSoup(html, "html.parser")
print(soup.findAll("div")[1])

# penggunaan beautifulsoup
from bs4 import BeautifulSoup

html = """
    <div>Ini paragraf kesatu Div</div>
    <p>Ini paragraf dengan sintag</p>
    <div>Ini paragraf kedua Div</div>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.p.text)  
print(soup)  
print(soup.div)  
print(soup.findAll("div"))  
print(soup.findAll("div")[1])  


from bs4 import BeautifulSoup
html = """
    <div>Ini paragraf kesatu Div</div>
    <p>Ini paragraf dengan sintag</p>
    <div class='bold'>Ini paragraf kedua Div</div>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.findAll("div",{'class':'bold'}))

print(soup.findAll("P",{"id","para"}))


from bs4 import BeautifulSoup

html = """
    <div id="d1" class="wide">
        <p id="p1"> ini adalah sintag paragraf</p>
        <img src=""/>
        <a id="a1"></a>
    </div>
    
    <div id="d2" class="small">
        <p id="p2"> ini adalah sintag paragraf kedua</p>
        <img src=""/>
        <a id="a2"></a>
    </div>

"""
soup = BeautifulSoup(html, "html.parser")
print(soup.findAll('div', {'id':'d2'})[0].p)

from bs4 import BeautifulSoup
html = """
    <div id="d1" class="wide">
        <p id="p1">This is a P</p>
        <div><p>OK</p></div>
        <img src=""/>
        <a id="a1"></a>
    </div>
    
    <div id="d1" class="small">
        <p id="p1">This is a P</p>
        <div><p>KO</p></div>
        <img src=""/>
        <a id="a1"></a>
    </div>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.find("div", {"class":"small"}).findAll("p")[1])

# LATIHAN
from bs4 import BeautifulSoup

html = """
    <div>div1</div>
    <div>div2</div>
    <div>div3</div>
    <div>div4</div>
    <div>div5</div>
    <div>div6</div>
    <div>div7</div>
    <div>div8</div>
    <div>div9</div>
    <div>div10</div>
"""

soup = BeautifulSoup(html, "html.parser")
# CARA 1
# div = soup.find_all("div")
# for i in range(1, len(div), 2):
#     print(div[i].text)

# CARA 2 
for index, div in enumerate(soup.findAll("div")) :
    if (index + 1) % 2 == 0 :
        print(div.text)



