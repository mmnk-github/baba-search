from bs4 import BeautifulSoup
import requests
import json
import sys

data = []

# Nouns
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Nouns")
soup = BeautifulSoup(res.content, features="lxml")

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
        if name == 'GROUP':
            for subimg in a.select("img"):
                subname = subimg["alt"][5:-6]
                if subname == 'GROUP2' or subname == 'GROUP3':
                    subgif = subimg["data-src"]
                    data.append({"name": subname, "gif": subgif})

# Operators
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Operators")
soup = BeautifulSoup(res.content, features="lxml")
for table in soup.select("table"):
    for tr in table.select("tr"):
        td = tr.find("td", style="text-align:center")
        if td == None:
            continue
        for img in td.select("img"):
            name = img["alt"][5:-6]
            if name == "IS":
                gif = img["src"]
            else:
                gif = img["data-src"]
            data.append({"name": name, "gif": gif})

# Properties
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Properties")
soup = BeautifulSoup(res.content, features="lxml")
for table in soup.select("table"):
    for tr in table.select("tr"):
        td = tr.select_one("td")
        if td == None:
            continue
        for img in td.select("img"):
            name = img["alt"][5:-6]
            gif = img["data-src"]
            data.append({"name": name, "gif": gif})

aisu = {}

for d in data:
    print(d['name'])
    aisu[d['name']] = {"sorted_name": sorted(d['name']), "img": "./image/" + d["name"] + ".gif"}
    r = requests.get(d["gif"])
    print(r)
    if r.status_code != 200:
        print("error")
        sys.exit(1)
    with open("./Pages/image/" + d["name"] + ".gif", "wb") as file:
        file.write(r.content)

with open("obj_name_data.json", 'w') as sym:
    json.dump(aisu, sym)

with open("obj_name_data.json", "r") as sym:
    obj_name_data = sym.read()

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
