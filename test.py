import requests
from bs4 import BeautifulSoup

url = "https://liquipedia.net/starcraft2/Marine_(Legacy_of_the_Void)"
html = requests.get(url).text

print(html)