import os
import asyncio
import aiosqlite
from typing import Optional, Dict, Union

class GeoDBFinder:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'data', 'geolocations.db')

    async def _search_location_async(self, city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Asynchronously search for a location in the database.
        
        Args:
            city_name (str): Name of the city to search for
            country (str, optional): Country name to filter results
            
        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found
        """
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            
            if country:
                query = """
                    SELECT city_name, longitude, latitude, timezone, country 
                    FROM records 
                    WHERE LOWER(city_name) = LOWER(?) AND LOWER(country) = LOWER(?)
                    LIMIT 1
                """
                cursor = await db.execute(query, (city_name, country))
            else:
                query = """
                    SELECT city_name, longitude, latitude, timezone, country 
                    FROM records 
                    WHERE LOWER(city_name) = LOWER(?)
                    LIMIT 1
                """
                cursor = await db.execute(query, (city_name,))
            
            result = await cursor.fetchone()
            
            if result:
                return {
                    'city': result['city_name'],
                    'longitude': result['longitude'],
                    'latitude': result['latitude'],
                    'timezone': result['timezone'],
                    'country': result['country']
                }
            return None

    def search_location(self, city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Synchronously search for a location in the database.
        
        Args:
            city_name (str): Name of the city to search for
            country (str, optional): Country name to filter results
            
        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found
        """
        return asyncio.run(self._search_location_async(city_name, country))

# Create a singleton instance
_finder = GeoDBFinder()

def search_location(city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
    """
    Search for a location by city name and optionally country.
    
    Args:
        city_name (str): Name of the city to search for
        country (str, optional): Country name to filter results
        
    Returns:
        Optional[Dict[str, str]]: Dictionary containing:
            - city: Name of the city
            - longitude: Longitude coordinate
            - latitude: Latitude coordinate
            - timezone: Timezone name
            - country: Country name
            
        Returns None if the city is not found.
        
    Example:
        >>> result = search_location("London", "United Kingdom")
        >>> print(result)
        {
            'city': 'London',
            'longitude': '0w07',
            'latitude': '51n30',
            'timezone': 'Europe/London',
            'country': 'United Kingdom'
        }
    """
    return _finder.search_location(city_name, country)

async def search_location_async(city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
    """
    Asynchronously search for a location by city name and optionally country.
    
    This is the async version of search_location(). Use this in async contexts.
    
    Args and return value are the same as search_location().
    
    Example:
        >>> result = await search_location_async("London", "United Kingdom")
    """
    return await _finder._search_location_async(city_name, country)
