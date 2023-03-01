import re
from bs4 import BeautifulSoup
import requests


# 1 - Find apartment links

x = 0
url = "https://www.morizon.pl/mieszkania/?ps%5Bwith_3d_view%5D=1&page="
# url = input("wprowadź url: ")
while x <= 91:
    x = str(x)
    result = requests.get(url + x)
    doc = BeautifulSoup(result.text, "html.parser")
    x = int(x)
    x += 1

    links = doc.find_all(href=re.compile("sprzedaz-mieszkanie"))

    links = str(links)

# 2 - Sort code by links and other code

    def Find(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)
        return [x[0] for x in url]

    string = links
    pure_links = Find(string)

# 3 Sort and extract 3d links

    for i in pure_links:
        result = requests.get(i)
        doc = BeautifulSoup(result.text, "html.parser")
        links_1 = doc.find_all("iframe")
        links_1 = str(links_1)

        def Find(string):
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, string)
            return [x[0] for x in url]
        end_links = Find(links_1)
        y = end_links[1]
        print(y)






