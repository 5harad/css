import requests
from bs4 import BeautifulSoup


def main():
  response = requests.get("https://www.imdb.com/chart/top?ref_=nv_ch_250_4")
  soup = BeautifulSoup(response.text)
  for td in soup.find_all('td', attrs={'class': 'titleColumn'}):
    title_link = td.find('a').get('href')
    print('https://www.imdb.com' + title_link)

if __name__ == '__main__':
  main()
