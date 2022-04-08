from wsgiref import headers
import requests, bs4
from requests.exceptions import HTTPError
import webbrowser
import sys

try:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
    }

    keywords = input("Informe a keyword:")

    r = requests.get(f'https://pypi.org/search/?q={keywords}', headers=headers)
    r.raise_for_status()

except HTTPError:
    print('Deu erro!!')
    sys.exit(1)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

lista_elem = soup.select('.package-snippet')

for elem in lista_elem:
    url_to_open = 'https://pypi.org' + elem.get('href')
    webbrowser.open(url_to_open)


