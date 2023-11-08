import requests

api_key = '86705dc9-1443-4d6a-b088-6151d633d37a'
word = 'orange'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)