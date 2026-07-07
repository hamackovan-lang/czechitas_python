##1.cast
#import balicku
import requests
import json
#input - osoba zada ico
ico = input("Zadej IČO: ")
#volani api - get
api_call = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = api_call.json()
#vypis
print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])

##2.cast
#import balicku
import json
import requests
nazev = input("Zadej název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"}
data = f'{{"obchodniJmeno": "{nazev}"}}'
#volani api - post
api_call = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
    headers=headers,
    data=data)

data = api_call.json()
print("Nalezeno subjektů:", data["pocetCelkem"])
for item in data["ekonomickeSubjekty"]:
    print(item["obchodniJmeno"], ",", item["ico"])
