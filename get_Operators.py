from bs4 import BeautifulSoup
import requests
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Operators")

soup = BeautifulSoup(res.content, features="lxml")

data = []
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
