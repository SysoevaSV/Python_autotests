import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2522e7af1bfc55818d54cd8050a7747f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7250'

body_registration = {
    "trainer_token": TOKEN,
    "email": "Sysoeva-svetaW@yandex.ru",
    "password": "Sysoevasv1996"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "122017",
    "name": "Бульба",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "122017"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)









