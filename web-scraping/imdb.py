import requests
import bs4

IMDB_TOP_250 = "https://www.imdb.com/chart/top?ref_=nv_ch_250_4"


def get_actors_and_characters(url):
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text)
  cast_table = soup.find('table', attrs={'class': 'cast_list'})
  actors, characters = [], []
  for row in cast_table.find_all('tr')[1:]:
    actors.append(row.find_all('td')[1].a.text.strip())
    try:
      characters.append(row.find('td', attrs={'class': 'character'}).a.text)
    except:
      characters.append(row.find('td', attrs={'class': 'character'}).text)
  return {'actors': actors, 'characters': characters}

def get_top_ten_movie_urls():
  response = requests.get(IMDB_TOP_250)
  soup = bs4.BeautifulSoup(response.text)
  lister_list = soup.find('tbody', attrs={'class': 'lister-list'})
  movie_links = []
  for movie_row in lister_list.find_all('tr'):
    href = movie_row.find('td', attrs={'class': 'titleColumn'}).a.get('href')
    movie_links.append(href)
  return movie_links[:10]

def get_all_actors_and_characters():
  casts = []
  for url in get_top_ten_movie_urls():
    # In reality, you should probably throttle these successive requests!
    casts.append(get_actors_and_characters("https://www.imdb.com" + url))
  return casts

def print_all_actors_and_characters():
  for url in get_top_ten_movie_urls():
    print(get_actors_and_characters("https://www.imdb.com" + url))
