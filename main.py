from urllib.parse import urljoin
import requests
import re
from bs4 import BeautifulSoup
url= "https://autbor.com/breadcrumbs/"


pattern = re.compile(r"\b[a-z]+\.html\b")
while True:
    print("Visiting:", url)
    response = requests.get(url)
    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    div = soup.find("div")

    if div:
        match = pattern.search(div.get_text())
        if match:
            filename = match.group().strip()
            url = urljoin(url,filename)
        else:
            print("Reached the end! Final message:", div.get_text().strip())
            break
    else:
        print("No <div> found on page.")
        break