"""записать конец ссылки на фото, а потом добавить к нему общее начало всех url"""
"""b5ea4714712d05e08254583fd8b23caf7a87570676babad5e58bcd93c609d724"""
"""https://evryplace.com/api/v1/files/stream/THUMBNAIL/"""
"""'https://files.evryplace.com/api/v1/files/stream/TUMBNAIL/'"""

url_1 = 'https://evryplace.com/api/v1/files/stream/THUMBNAIL/'


url_2 = 'https://evryplace.com/embed/orodmx'



import re
import requests
from bs4 import BeautifulSoup

url = url_2
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")

# result = doc.find_all(string=re.compile('spheres'))
result = doc.find_all(string=re.compile("hash"))
result = str(result)
print(result)
splited_result = result.split(',')
for i in splited_result:
    if "hash" in i:
        pass

        hash = i.split('"')
        print(url_1 + hash[3])







