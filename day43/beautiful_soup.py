from bs4 import BeautifulSoup

with open("day43/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
print(soup.prettify())

all_anchor = soup.find_all(name="a")

for tag in all_anchor:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)