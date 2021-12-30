import requests, json

user = str(input("Digite seu user no GitHub:"))
response = requests.get(f"https://api.github.com/users/{user}/repos")

repositorios = list(map(lambda resp: {'name': resp["name"]}, response.json()))

with open(f'{user}.json',"w") as file:
    json.dump(repositorios, file)