import pytest
from geodb_finder import search_location, search_location_async, list_countries, list_countries_async

def test_sync_search():
    # Test synchronous search
    result = search_location("Amsterdam")
    print("Sync search result:", result)
    assert result is not None
    assert result["city"] == "Amsterdam"
    assert result["country"] == "Netherlands"
    assert "longitude" in result
    assert "latitude" in result
    assert "timezone" in result

    # Test with country filter
    result = search_location("London", "United Kingdom")
    print("Sync search with country result:", result)
    assert result is not None
    assert result["city"] == "London"
    assert result["country"] == "United Kingdom"

def test_list_countries():
    # Test synchronous list_countries
    countries = list_countries()
    print("Sync list_countries result:", countries)
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert "Netherlands" in countries  # Example check

@pytest.mark.asyncio
async def test_list_countries_async():
    # Test asynchronous list_countries_async
    countries = await list_countries_async()
    print("Async list_countries result:", countries)
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert "Netherlands" in countries  # Example check

    # Test asynchronous search
    result = await search_location_async("Amsterdam")
    print("Async search result:", result)
    assert result is not None
    assert result["city"] == "Amsterdam"
    assert result["country"] == "Netherlands"
    assert "longitude" in result
    assert "latitude" in result
    assert "timezone" in result

    # Test with country filter
    result = await search_location_async("London", "United Kingdom")
    print("Async search with country result:", result)
    assert result is not None
    assert result["city"] == "London"
    assert result["country"] == "United Kingdom"
