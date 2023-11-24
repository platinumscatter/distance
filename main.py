import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, red, yellow

walking_emoji = "🏃"
bus_emoji = "🚌"
plane_emoji = "✈"

print(blue("Welcome to the distance calculator!\n"))

first_city = inquirer.prompt([
    inquirer.Text('name', message="Enter the name of the first city:"),
    inquirer.Text('country', message="Enter the name of the first country:")
])
second_city = inquirer.prompt([
    inquirer.Text('name', message="Enter the name of the second city:"),
    inquirer.Text('country', message="Enter the name of the second country:")
])

first_location = f"{first_city['name'], {first_city['country']}}"
first_coords = geocoders.Nominatim(user_agent="distance_calculator").geocode(first_location).point
second_location = f"{second_city['name'], {second_city['country']}}"
second_coords = geocoders.Nominatim(user_agent="distance_calculator").geocode(second_location).point

walk_distance_km = distance.distance(first_coords, second_coords).km
bus_distance_km = distance.distance(first_coords, second_coords).km
air_distance_km = distance.distance(first_coords, second_coords).km

walk_distance_miles = distance.distance(first_coords, second_coords).miles
bus_distance_miles = distance.distance(first_coords, second_coords).miles
air_distance_miles = distance.distance(first_coords, second_coords).miles

walk_time = walk_distance_km / 5
bus_time = bus_distance_km / 60
air_time = air_distance_km / 800

print(green('\nResults:'))
print(f"Distance between {first_location} and {second_location} by:")
print(yellow(f" {walking_emoji} Walking: {walk_distance_km:.2f} Km / {walk_distance_miles:.2f} Miles, time: {walk_time:.2f} hours"))
print(yellow(f" {bus_emoji} Bus: {bus_distance_km:.2f} Km / {bus_distance_miles:.2f} Miles, time: {bus_time:.2f} hours"))
print(yellow(f" {plane_emoji}  Airplane: {air_distance_km:.2f} Km / {air_distance_miles:.2f} Miles, time: {air_time:.2f} hours"))
