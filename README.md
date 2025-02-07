# geodb-finder

A Python package to find timezone and coordinates for cities worldwide.

## Installation

```bash
pip install geodb-finder
```

## Usage

```python
from geodb_finder import search_location

# Search for a city
result = search_location("London")
print(result)  # Returns dict with longitude, latitude, and timezone

# Search with country filter
result = search_location("London", country="United Kingdom")
print(result)
```
