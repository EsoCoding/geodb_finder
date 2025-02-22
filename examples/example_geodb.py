from geodb_finder import search_location

# Search for a city
results = search_location("London")
if results:
    city_info = results[0]  # Get the first match
    
print(city_info)  # Dictionary with latitude, longitude, timezone, and country
