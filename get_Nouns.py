from bs4 import BeautifulSoup
import requests
import json
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Nouns")

soup = BeautifulSoup(res.content, features="lxml")

data = []
for article_table in soup.select(".article-table"):
    for tr in article_table.select("tr"):
        if tr.select_one("td") == None:
            continue
        name = tr.select_one("td").text[0: -1]
        for img in tr.select("img"):
            gif = img['data-src']
        data.append({"name": name, "gif": gif})

table = soup.select_one(".table")
for a in table.select("tr"):
    img = a.select_one("img")
    if img != None:
        name = img["alt"][5:-6]
        gif = img["data-src"]
        data.append({"name": name, "gif": gif})

aisu = {}

for d in data:
    aisu[d['name']] = {"sorted_name": sorted(d['name']), "img": "./image/" + d["name"] + ".gif"}
    # r = requests.get(d["gif"])
    # print(r)
    # with open("./Pages/image/" + d["name"] + ".gif", "wb") as file:
    #     file.write(r.content)

with open("obj_name_data.json", 'w') as sym:
    json.dump(aisu, sym)

with open("obj_name_data.json", "r") as sym:
    obj_name_data = sym.read()
    print(obj_name_data)

with open("obj_name_data.json.js", "w") as sym:
    sym.write("let obj_name_data = " + obj_name_data + ";")

# {
#     "FOFO": {
#         "sorted_name": "OOFF",
#         "img": "FOFO.gif"
#     },
#     "BABA": {
#         "sorted_name": "AABB",
#         "img": "BABA.gif"
#     }
# }
