import json

with open("animals_template.html", "r") as file:
    content = file.read()
    print(content)


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals = load_data('animals_data.json')


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


animals_info = ""
for animal_obj in animals:
    animals_info += serialize_animal(animal_obj)

final_html = content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w") as output_file:
    output_file.write(final_html)

print("HTML file generated successfully")
