import requests
import datetime as dt

USERNAME = "nurmatthias"
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GRAPH_ID = "graph-coding"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


create_user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=PIXELA_ENDPOINT, json=create_user)
#print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "CodingGraph",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
#response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
#print(response)

now = dt.datetime.now()
post_data = {
    "date": now.strftime("%Y%m%d"),
    "quantity": "1",
}
response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=post_data, headers=HEADERS)
print(response)