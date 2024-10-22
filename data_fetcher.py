import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {
        "X-Api-Key": API_KEY
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