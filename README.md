# geodb-finder

`geodb-finder` is a Python package that allows you to retrieve geographical information such as latitude, longitude, timezone ID, and country using a city or location name. Additionally, it supports searching for the same information using latitude and longitude.

## Installation

Install the package using pip:

```bash
pip install geodb-finder
```

## Usage

### Find Location Information by City Name

You can retrieve latitude, longitude, timezone ID, and country by providing a city name.

```python
from geodb_finder import search_location

# Search for a city
result = search_location("London")
print(result)  # Returns a list of dictionaries with latitude, longitude, timezone, and country
```

Results are returned as a list of dictionaries, where each dictionary contains:
- `city`: The city name
- `country`: The country name
- `latitude`: The latitude coordinate
- `longitude`: The longitude coordinate
- `timezone`: The timezone identifier

**Note:** An asynchronous version of this function is available as `search_location_async(city_name: str, country: Optional[str] = None)`.

### Find Location Information by Coordinates

You can also retrieve location details using latitude and longitude coordinates. The function supports returning multiple results.

```python
from geodb_finder import search_by_coordinates

# Search by latitude and longitude
results = search_by_coordinates("52n22", "4e53", limit=3)  # Example: Amsterdam with multiple results
print(results)  # Returns a list of dictionaries with city, latitude, longitude, timezone, and country
```

**Note:** An asynchronous version of this function is available as `search_by_coordinates_async(latitude: str, longitude: str, limit: int = 1)`.

**Important:** The database stores coordinates in a specific format (e.g., `"52n22"`, `"4e53"`). Ensure you use the correct format when querying.

### List Available Countries

You can retrieve a list of all available countries in the database.

```python
from geodb_finder import list_countries

countries = list_countries()
print(countries)  # Returns a list of dictionaries with 'country' key
```

**Note:** An asynchronous version of this function is available as `list_countries_async()`.

## Running Tests

To run the test suite, use:

```bash
pytest
```

Ensure you have `pytest` installed:

```bash
pip install pytest
