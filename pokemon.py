import requests
from constant_url import BASE_URL
from pokemon_queries import insert_data

 
#Send a GET request to the PokeAPI endpoint for retrieving information about Pokemon

def populate_pokemon_data(url=None):
    if url:
        response = requests.get(url=url)
    else:
        response = requests.get(url=BASE_URL)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:            
        response_data = response.json()        
        next_url = response_data.get("next")
        result = response_data.get("results")

        # Iterate over each Pokemon in the list & store the db
        for row in result:                     
            pokemon_name = row.get("name")
            details_url = row.get("url")
            detail_response = requests.get(    
                url=details_url
            )

            if detail_response.status_code == 200:   
                details = detail_response.json()

                # create pokemon abilities string
                abilities =[]
                for ability in details.get("abilities"):
                    abilities.append(ability.get("ability").get("name"))

                abilities = ", ".join(abilities)

                # create pokemon type string
                pokemon_type =[]
                for type in details.get("types"):  
                    pokemon_type.append(type.get("type").get("name"))

                pokemon_type = ", ".join(pokemon_type)
                    
                # create pokemon moves data str
                pokemon_moves =[]
                for move in details.get("moves"):  
                    pokemon_moves.append(move.get("move").get("name"))

                pokemon_moves = ", ".join(pokemon_moves)

                # fetch pokemon species data
                pokemon_species_str = details.get("species").get("name")

                pokemon_weight = []
                pokemon_weight = str(details.get("weight"))

                pokemon_hieght = []
                pokemon_hieght = str(details.get("height"))

                pokemon_forms = []
                for forms in details.get("forms"):
                    pokemon_forms.append(forms.get("name"))

                pokemon_forms = ", ".join(pokemon_forms)

                # Construct a dictionary containing information about a Pokemon

                pokemon = dict(
                    name=pokemon_name,             # Name of the Pokemon
                    abilities=abilities,           # List of abilities of the Pokemon
                    type=pokemon_type,             # Type(s) of the Pokemon
                    species=pokemon_species_str,   # Species of the Pokemon
                    weight=pokemon_weight,         # Weight of the Pokemon
                    hieght=pokemon_hieght,         # Height of the Pokemon
                    moves=pokemon_moves,           # List of moves known by the Pokemon
                    forms=pokemon_forms            # List of forms of the Pokemon
                    )
                # Insert the data of the Pokemon into a database

                insert_data(pokemon)

        return next_url

next_url = None
for i in range(20):
    if next_url:
        next_url = populate_pokemon_data(url=next_url)
    else:
        next_url = populate_pokemon_data()
