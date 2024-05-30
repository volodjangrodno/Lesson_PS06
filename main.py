import requests
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/top/bestofrt/?year=2019"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")
data = []

for row in rows:
    cols = row.find_all("td")
    cleaned_cols = [col.text.strip() for col in cols]
    data.append(cleaned_cols)

print(data)