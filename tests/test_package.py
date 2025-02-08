import pytest
from geodb_finder import search_location, search_location_async

def test_sync_search():
    # Test synchronous search
    result = search_location("Amsterdam")
    assert result is not None
    assert result["city"] == "Amsterdam"
    assert result["country"] == "Netherlands"
    assert "longitude" in result
    assert "latitude" in result
    assert "timezone" in result

    # Test with country filter
    result = search_location("London", "United Kingdom")
    assert result is not None
    assert result["city"] == "London"
    assert result["country"] == "United Kingdom"

@pytest.mark.asyncio
async def test_async_search():
    # Test asynchronous search
    result = await search_location_async("Amsterdam")
    assert result is not None
    assert result["city"] == "Amsterdam"
    assert result["country"] == "Netherlands"
    assert "longitude" in result
    assert "latitude" in result
    assert "timezone" in result

    # Test with country filter
    result = await search_location_async("London", "United Kingdom")
    assert result is not None
    assert result["city"] == "London"
    assert result["country"] == "United Kingdom"
