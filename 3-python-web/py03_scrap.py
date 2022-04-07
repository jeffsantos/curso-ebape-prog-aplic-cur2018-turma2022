import requests, bs4
from requests.exceptions import HTTPError
import webbrowser
import sys

try:

    keywords = input("Informe a keyword:")
    r = requests.get(f'https://pypi.org/search/?q={keywords}')
    r.raise_for_status()

except HTTPError:
    print('Deu erro!!')
    sys.exit(1)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

lista_elem = soup.select('.package-snippet')

for elem in lista_elem:
    url_to_open = 'https://pypi.org' + elem.get('href')
    webbrowser.open(url_to_open)


