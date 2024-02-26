import subprocess
import requests


# Ustawienia autoryzacji i nagłówki
CLIENT_ID = '99d7d0fcf8ba4ebea83c9af7954b89be'
CLIENT_SECRET = 'e3751ff3c4cd4c93b88a6a40b91ab3fa'
AUTH_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1'
playlist_id = '1WdUGMG1CIBmoFTNyiirJx'



# Pobierz token autoryzacyjny
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

# Nagłówki dla zapytania do API
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Zapytanie o informacje o playliście
playlist_response = requests.get(f'{API_BASE_URL}/playlists/{playlist_id}/tracks?fields=items(track(name,artists(name)))', headers=headers)

# Pobierz listę piosenek z odpowiedzi API
playlist_data = playlist_response.json()

# Zapisz listę piosenek do pliku tekstowego
with open('lista_piosenek.txt', 'w', encoding='utf-8') as f:
    for item in playlist_data['items']:
        f.write(f"{item['track']['name']} - {item['track']['artists'][0]['name']}\n")

print("Uruchamianie: main.py")

subprocess.run(['C:\\Users\\filop\\.pyenv\\pyenv-win\\versions\\3.11.1\\python3.11.exe','C:\Programing\python\Song_Downolander\main.py'], check=True)