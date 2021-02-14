from bs4 import BeautifulSoup
import requests
res = requests.get("https://babaiswiki.fandom.com/wiki/Category:Properties")

soup = BeautifulSoup(res.content, features="lxml")
