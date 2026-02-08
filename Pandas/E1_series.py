import pandas as pd

pokedoc = {"1": "Pikachu",
            "2": "Bulbasaur",
            "3": "Charmander",
            "4": "Squirtle"}

#add dictionary to series
series = pd.Series(pokedoc)
print(series)

#filtering series with index keys that are even and odd
even_pokemon = series[series.index.astype(int) % 2 == 0]
print("even_pokemon:")
print(even_pokemon)

odd_pokemon = series[series.index.astype(int) % 2 != 0]
print("odd_pokemon:")
print(odd_pokemon)

#setting up custom index
series.index = ["Electric", "Grass", "Fire", "Water"]
print(series)


#setting up name to series
series.name = "Pokemon"
print(series)   #prints only the name of the series, not the data

#print as before setting up a name to series
print(series.to_string())   #prints the data of the series without the name of the series
