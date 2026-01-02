#Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#ea el archivo JSON
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
#Calcule y muestre el promedio de nivel para cada tipo:

import json

def read_pokemon_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)
    return pokemon_data 

def calculate_average_stats_per_pokemon(pokemon_list):
    pokemon_averages = []
    
    for pokemon in pokemon_list:
        name = pokemon.get('name', {}).get('english', 'Unknown')
        types = pokemon.get('type', [])
        base_stats = pokemon.get('base', {})
        
        stats_values = list(base_stats.values())
        if stats_values:
            pokemon_avg = sum(stats_values) / len(stats_values)
        else:
            pokemon_avg = 0
        
        pokemon_averages.append({
            'name': name,
            'types': types,
            'average': pokemon_avg
        })
    
    return pokemon_averages

def calculate_average_stats_by_type(pokemon_averages):
    type_stats = {}
    
    for pokemon in pokemon_averages:
        types = pokemon['types']
        pokemon_avg = pokemon['average']
        
        for t in types:
            if t not in type_stats:
                type_stats[t] = []
            type_stats[t].append(pokemon_avg)
    
    average_stats = {}
    for t, avg_list in type_stats.items():
        average_stats[t] = sum(avg_list) / len(avg_list)
    
    return average_stats

def display_average_stats(average_stats):
    print("\n   Average Stats by Pokémon Type :")
    for t, avg_stat in sorted(average_stats.items()):
        print(f"Type: {t}, Average Stats: {avg_stat:.2f}")

def main():
    file_path = 'pokemon_data.json'  
    pokemon_list = read_pokemon_json(file_path)
    pokemon_averages = calculate_average_stats_per_pokemon(pokemon_list)
    average_stats = calculate_average_stats_by_type(pokemon_averages)
    display_average_stats(average_stats)    

if __name__ == "__main__":
    main()