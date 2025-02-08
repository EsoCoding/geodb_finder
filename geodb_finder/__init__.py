import os
import logging
import asyncio
import aiosqlite
from typing import Optional, Dict, List, Any


# Configure logging
logging.basicConfig(level=logging.DEBUG)

class GeoDBFinder:
    """Handles database interactions for geolocation data."""

    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), "data", "geolocations.db")

    async def _fetch_one(self, query: str, params: tuple) -> Optional[Dict[str, str]]:
        """Executes a query and returns a single result as a dictionary."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params)
            result = await cursor.fetchone()
            return dict(result) if result else None

    async def _fetch_all(self, query: str) -> List[Dict[str, str]]:
        """Executes a query and returns all results as a list."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query)
            results = await cursor.fetchall()
            return [row["country"] for row in results]

    async def search_location_async(self, city_name: str, country: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Asynchronously searches for a location in the database.

        Args:
            city_name (str): Name of the city to search for.
            country (Optional[str]): Country name to filter results.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found.
        """
        query = """
            SELECT city_name, longitude, latitude, timezone, country 
            FROM records 
            WHERE LOWER(city_name) = LOWER(?)
        """
        params = (city_name,)

        if country:
            query += " AND LOWER(country) = LOWER(?)"
            params += (country,)

        query += " LIMIT 1"
        result = await self._fetch_one(query, params)
        logging.debug(f"Query result for {city_name}, {country}: {result}")
        if result:
            result["city"] = result.pop("city_name")
        return result

    def search_location(self, city_name: str, country: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Synchronously searches for a location in the database.

        Args:
            city_name (str): Name of the city to search for.
            country (Optional[str]): Country name to filter results.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found.
        """
        return asyncio.run(self.search_location_async(city_name, country))

    async def search_by_coordinates_async(self, latitude: str, longitude: str) -> Optional[Dict[str, Any]]:
        """
        Asynchronously searches for a location in the database using latitude and longitude.

        Args:
            latitude (str): Latitude coordinate.
            longitude (str): Longitude coordinate.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found.
        """
        query = """
            SELECT city_name, longitude, latitude, timezone, country 
            FROM records 
            WHERE latitude = ? AND longitude = ?
            LIMIT 1
        """
        params = (latitude, longitude)
        result = await self._fetch_one(query, params)
        logging.debug(f"Query result for {latitude}, {longitude}: {result}")
        if result:
            result["city"] = result.pop("city_name")
        return result

    def search_by_coordinates(self, latitude: str, longitude: str) -> Optional[Dict[str, Any]]:
        """
        Synchronously searches for a location in the database using latitude and longitude.

        Args:
            latitude (str): Latitude coordinate.
            longitude (str): Longitude coordinate.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found.
        """
        return asyncio.run(self.search_by_coordinates_async(latitude, longitude))

        """
        Synchronously searches for a location in the database.

        Args:
            city_name (str): Name of the city to search for.
            country (Optional[str]): Country name to filter results.

        Returns:
            Optional[Dict[str, str]]: Dictionary containing location data or None if not found.
        """
        return asyncio.run(self.search_location_async(city_name, country))

    async def list_countries_async(self) -> List[Dict[str, str]]:
        """
        Asynchronously fetches a list of distinct country names from the database.

        Returns:
            List[str]: A list of country names.
        """
        query = "SELECT DISTINCT country FROM records ORDER BY country"
        return await self._fetch_all(query)

    def list_countries(self) -> List[Dict[str, str]]:
        """
        Synchronously fetches a list of distinct country names from the database.

        Returns:
            List[Dict[str, str]]: A list of country names.
        """
        return asyncio.run(self.list_countries_async())


# Singleton instance
_finder = GeoDBFinder()

# Public API functions
def search_location(city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
    """Search for a location by city name and optionally country."""
    return _finder.search_location(city_name, country)


async def search_location_async(city_name: str, country: Optional[str] = None) -> Optional[Dict[str, str]]:
    """Asynchronously search for a location by city name and optionally country."""
    return await _finder.search_location_async(city_name, country)


def search_by_coordinates(latitude: str, longitude: str) -> Optional[Dict[str, Any]]:
    """Search for a location by latitude and longitude."""
    return _finder.search_by_coordinates(latitude, longitude)

async def search_by_coordinates_async(latitude: str, longitude: str) -> Optional[Dict[str, Any]]:
    """Asynchronously search for a location by latitude and longitude."""
    return await _finder.search_by_coordinates_async(latitude, longitude)

    """Fetch a list of distinct country names from the database."""
    return _finder.list_countries()


def list_countries() -> List[str]:
    """Fetch a list of distinct country names from the database."""
    return _finder.list_countries()

async def list_countries_async() -> List[str]:
    """Asynchronously fetch a list of distinct country names from the database."""
    return await _finder.list_countries_async()
