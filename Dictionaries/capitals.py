countries = input().split(", ")
capitals = input().split(", ")

country_capital = {countries: capitals for (countries,capitals) in zip(countries, capitals)}

for country, capital in country_capital.items():
    print(f"{country} -> {capital}")
