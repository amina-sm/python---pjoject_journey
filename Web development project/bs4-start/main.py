from bs4 import BeautifulSoup
import requests

responses = requests.get("https://news.ycombinator.com/news")
yc_web_page = responses.text
# print(responses.text)

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)


# with open("bs4-start/website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup=BeautifulSoup(contents,"html.parser")
# #print(soup.title.string)

# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading=soup.find(name="h1", id="name")
# print(heading)

# section_heading=soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url=soup.select_one(selector="p a")
# print(company_url)
