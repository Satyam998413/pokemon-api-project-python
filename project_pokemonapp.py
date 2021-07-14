# Ask  for user input pokemon name
import requests
# create a dynamicurl based on step 1
# fetch the data from the url
# convert json to a dic
# print pockemon data
while True:
    pokemon=input("Which pokemon do you Find?")
    pokemon=pokemon.lower()

    url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req=requests.get(url)

    if req.status_code==200:

        data=req.json()
        ponam=data['name']
        print("Name is \t \t ",ponam)
        print("Abilities")
        for ability in data['abilities']:
            print(ability['ability']['name'])

    else:
        print("Pokemon not found")