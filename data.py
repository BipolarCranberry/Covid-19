import urllib.request


def update_data():
    url = 'https://raw.githubusercontent.com/Daniel-Breuss/covid-data-austria/master/austriadata.csv'
    urllib.request.urlretrieve(url, './Data/data-austria.csv')

