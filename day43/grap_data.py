from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.select(".storylink")
article_add_data = soup.select("span.score")

article_texts = []
article_links = []
for tag in article_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))

article_points = [int(data.getText().split()[0]) for data in article_add_data]

print(article_texts)
print(article_links)
print(article_points)

max_index = article_points.index(max(article_points))

print(article_texts[max_index])
print(article_links[max_index])
print(article_points[max_index])