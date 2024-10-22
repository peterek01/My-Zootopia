import data_fetcher

animal_name = input("Enter an animal: ")
animals = data_fetcher.fetch_data(animal_name)

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


if animals:
    animals_info = ''
    for animal_obj in animals:
        animals_info += serialize_animal(animal_obj)
else:
    animals_info = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

final_html = content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w") as output_file:
    output_file.write(final_html)

print("HTML file generated successfully.")

