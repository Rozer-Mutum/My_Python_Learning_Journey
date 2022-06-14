travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#Do NOT change the code above

#TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
def add_new_country(country_visited, visits_number, cities_visited):
    new_dictionary = {}
    new_dictionary["country"] = country_visited
    new_dictionary["visits"] = visits_number
    new_dictionary["cities"] = cities_visited
    # print(new_dictionary)
    travel_log.append(new_dictionary)


#Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)