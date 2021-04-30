from bs4 import BeautifulSoup
from googlesearch import search

# to search
print("What you want to search")
query = input()
import webbrowser
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
	webbrowser.open(j)
