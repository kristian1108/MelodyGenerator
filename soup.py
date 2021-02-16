from bs4 import BeautifulSoup
import requests

url = "https://www.hendersoncountync.gov/health/page/covid-19-vaccines"
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
