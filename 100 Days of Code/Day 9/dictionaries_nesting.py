# Nesting Dictionary in a Dictionary
capitals = {
    "France":"Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits": 12},

    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stutgart"],
    "total_visits": 8}
}

print(travel_log)

# Nesting dictionary in a list
travel_log = [
    {
    "country": "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {
    "country": "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stutgart"], 
    "total_visits": 8
    },
]

for country in travel_log:
    print(country["country"])
    print(country["cities_visited"])
    print(country["total_visits"])