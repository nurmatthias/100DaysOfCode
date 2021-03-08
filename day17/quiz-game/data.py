import requests

url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

response = requests.get(url)

data = response.json()

question_data = data["results"]