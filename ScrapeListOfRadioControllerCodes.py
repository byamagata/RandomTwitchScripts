import requests
from bs4 import BeautifulSoup

page = requests.get("https://contests.arrl.org/contestmultipliers.php?a=wve")
soup  = BeautifulSoup(page.content, 'html.parser')

tabledata = soup.find_all('td')

codes = []
for i in range(len(tabledata)):
    if len(tabledata[i].get_text()) <= 3:
        if tabledata[i].get_text().strip() != "":
            codes.append(tabledata[i].get_text())


for i in codes:
    print(i)

