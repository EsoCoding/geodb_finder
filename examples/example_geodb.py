from geodb_finder import search_location

# Search for a city
print("Searching for London...\n")
results = search_location("London")
if results:
    city_info = results[0]  # Get the first match
    print(f"{city_info}\n")  # Dictionary with latitude, longitude, timezone, and country

# Search for a city with multiple results
print("Searching for Amsterdam...\n")
# Search with country filter
results = search_location("Amsterdam", country="Netherlands")
if results:
    city_info = results[0]
    print(f"Found: {city_info['city']}, {city_info['country']}\n")

print("Searching for non existing city\n")
# Search for a city that does not exist
results = search_location("Non-existing city")
if not results:
    print("City not found")