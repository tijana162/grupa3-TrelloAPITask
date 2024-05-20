import requests
import json

# API ključ i token koje ste generisali na Trello-u
API_KEY = "129c1351c51bed7ad05d9780f6c1567f"
TOKEN = "ATTA31202f574dbe08de9bdcdaec86836037a7ad507f4523f6e7c4b638251dcafaa78D724935"

# ID table na kojoj radite - možete ga pronaći u URL-u Trello board-a
BOARD_ID = "osg1e806"
cards=["pr9XkAUT","3rwLc1dd","v1MP3Bep"]

# Funkcija za dobijanje informacija o svim karticama na Trello board-u
def get_cards():
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"
    query = {"key": API_KEY, "token": TOKEN}
    response = requests.get(url, params=query)
    if response.status_code == 200:
        cards = response.json()
        return cards
    else:
        print("Failed to retrieve cards.")
        return None

# Funkcija za dodavanje nove kartice na Trello board
def add_card(name, description):
    url = "https://api.trello.com/1/cards"
    query = {"key": API_KEY, "token": TOKEN, "idList": BOARD_ID, "name": name, "desc": description}
    response = requests.post(url, params=query)
    if response.status_code == 200:
        print("Card added successfully.")
    else:
        print("Failed to add card.")


    # Dodavanje nove kartice
    new_card_name = "New Task"
    new_card_description = "Description of the new task"
    add_card(new_card_name, new_card_description)
