import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_web_page = response.text
# print(movies_web_page)

soup = BeautifulSoup(movies_web_page, "html.parser")

movies_container = soup.find("div", class_="article__body")

movie_items = movies_container
movie_items = soup.find_all('li')

# Extract movie titles
movies = [item.text.strip() for item in movie_items]
with open('movies.txt', 'w') as file:
    for i, movie in enumerate(movies[:100], start=1):
        file.write(f"{i}. {movie}\n")

    print("Movie titles saved to movies.txt")
