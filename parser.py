import requests
from bs4 import BeautifulSoup

Dollar_url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=15&beg_day=01&beg_month=01&beg_year=2021&end_day=10&end_month=01&end_year=2021'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find('div', class_='col-md-10 col-sm-12 col-xs-12 content-cont').find('table')
    for val in tables:
        try:
            date = val.find('td').text
            return date
        except:
            table = 'No items'
        try:
            value = val.find('td', class_='stat-right').text
            return value
        except:
            value = 'No items'
def main():
    get_page_data(get_html(Dollar_url))
    


if __name__ == '__main__':
    main()
