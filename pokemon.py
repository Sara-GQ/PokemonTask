import requests
from constant_url import Base_url
from pokemon_queries import insert_data

 #Send a GET request to the PokeAPI endpoint for retrieving information about Pokemon

response = requests.get(
    url=Base_url
)
if response.status_code == 200:            # Check if the response is successful (status code 200)
    response_data = response.json()        # Extract JSON data from the response
    result = response_data.get("results")  # Extract the list of Pokemon from the JSON data

    for row in result:                     # Iterate over each Pokemon in the list
        print(row.get("name"))
        pokemon_name = row.get("name")     # Store the name of the Pokemon in a variable
        details_url = row.get("url")       # Extract the URL for detailed information about the Pokemon
        detail_response = requests.get(    
            url=details_url
        )

        if detail_response.status_code == 200:   
            details = detail_response.json()
 
            abilities =[]                       # Initialize an empty list to store the abilities of the Pokemon
            for ability in details.get("abilities"):    # Iterate over each Pokemon in the list
                abilities.append(ability.get("ability").get("name"))   # Extract and append the name of the ability to the list

            print(", ".join(abilities), end='\n\n')
            abilities = ", ".join(abilities)

            pokemon_type =[]
            for type in details.get("types"):  
                pokemon_type.append(type.get("type").get("name"))

            print(", ".join(pokemon_type), end='\n\n')
            pokemon_type = ", ".join(pokemon_type)
                
            
            pokemon_moves =[]
            for move in details.get("moves"):  
                pokemon_moves.append(move.get("move").get("name"))

            print(", ".join(pokemon_moves), end='\n\n')
            pokemon_moves = ", ".join(pokemon_moves)

            
            pokemon_species_str = details.get("species").get("name")


            pokemon_weight = []
            weight = details.get("weight")
            if (weight, int):
             pokemon_weight.append(weight)
            print(", ".join(map(str, pokemon_weight)), end='\n\n') 
            pokemon_weight = ", ".join(map(str, pokemon_weight))


            pokemon_hieght = []
            height = details.get("height")
            if (height, int):
             pokemon_hieght.append(height)
             print(", ".join(map(str, pokemon_hieght)), end='\n\n')  
             pokemon_hieght = ", ".join(map(str, pokemon_hieght))

            pokemon_forms = []
            for forms in details.get("forms"):
                pokemon_forms.append(forms.get("name"))

            print(", ".join(pokemon_forms), end='\n\n')
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