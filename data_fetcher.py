import requests

api_key = 'wm7dAuEaYpR3+Yck/Pz1/Q==GbXw4cWRi3NwahkI'


def fetch_data(animal_name):
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {
        "X-Api-Key": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        animals = response.json()
        if len(animals) == 0:
            return None
        else:
            return animals
    else:
        print(f"Failed to retrieve data from API. Status code: {response.status_code}")
        return None