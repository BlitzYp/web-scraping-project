from bs4 import BeautifulSoup
import requests
import csv
import pdb


def get_html(site: str):
    res = requests.get(site)
    return res.text


def clean(html):
    soup = BeautifulSoup(html, "html.parser")
    articles: list = soup.find_all('article')
    title: list = [a.find('a').get_text() for a in articles]
    date: list = [a.find('time')['datetime'] for a in articles]
    href: list = [a.find('a')['href'] for a in articles]
    return title, date, href


def write_to_csv(**kwargs):
    file: str = kwargs.get('file')
    if file:
        html, dates, href = kwargs.get('html'), kwargs.get(
            'dates'), kwargs.get('href')
        with open(kwargs.get('file'), 'w') as f:
            writer = csv.writer(f)
            for i in range(len(html)):
                writer.writerow([html[i], dates[i], href[i]])
        return print(f'finished writing {len(html)} articles to {file}')
    return print('Please provide a file!')


def main():
    site: str = "https://www.rithmschool.com/blog"
    html: list = get_html(site)
    data, dates, hrefs = clean(html)
    write_to_csv(file='data.csv', html=data, dates=dates, href=hrefs)


if __name__ == "__main__":
    main()

