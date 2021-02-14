from bs4 import BeautifulSoup
import requests
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
        print(img)
        name = img["alt"][5:-6]
        gif = img["data-src"]
        data.append({"name": name, "gif": gif})

# for d in data:
#     r = requests.get(d["gif"])
#     print(r)
#     with open("./Pages/image/" + d["name"] + ".gif", "wb") as file:
#         file.write(r.content)
