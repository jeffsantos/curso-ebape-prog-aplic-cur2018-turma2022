import requests
import sys

r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

if r.status_code != 200:
    print('Deu erro!!')
    sys.exit(1)

f = open('covid.csv', 'wb')

for chunk in r.iter_content(1000):
    f.write(chunk)

f.close()