import json
import requests

api_key = 'wm7dAuEaYpR3+Yck/Pz1/Q==GbXw4cWRi3NwahkI'

animal_name = input("Enter an animal: ")

url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'

headers = {
    "X-Api-Key": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    animals = response.json()
    if animals:
        print("Data fetched successfully from API")
    else:
        print("No data found for the given animal.")
else:
    print(f"Failed to retrieve data from API. Status code: {response.status_code}")
    exit()


with open('animals_template.html', 'r') as file:
    content = file.read()


def serialize_animal(animal_obj):
    name = animal_obj["name"]
    diet = animal_obj["characteristics"]["diet"]
    location = animal_obj["locations"][0]
    type_info = animal_obj["characteristics"].get("type", "Unknown")

    return f'''
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <p class="card__text">
                 <ul>
                    <li><strong>Diet:</strong> {diet}</li>
                    <li><strong>Location:</strong> {location}</li>
                    <li><strong>Type:</strong> {type_info}</li>
                </ul>
            </p>
         </li>
    '''


animals_info = ''
for animal_obj in animals:
    animals_info += serialize_animal(animal_obj)

final_html = content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals_web_api.html", "w") as output_file:
    output_file.write(final_html)

print("HTML file generated successfully.")