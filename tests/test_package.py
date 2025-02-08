import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import asyncio
from geodb_finder import search_location, search_location_async

def test_sync():
    # Test synchronous search
    print("\nTesting synchronous search:")
    result = search_location("Angul")
    print(f"Search for 'Angul': {result}")
    
    result = search_location("London", "United Kingdom")
    print(f"Search for 'London' in UK: {result}")

async def test_async():
    # Test asynchronous search
    print("\nTesting asynchronous search:")
    result = await search_location_async("Angul")
    print(f"Search for 'Angul': {result}")
    
    result = await search_location_async("London", "United Kingdom")
    print(f"Search for 'London' in UK: {result}")

if __name__ == "__main__":
    # Run sync tests
    test_sync()
    
    # Run async tests
    asyncio.run(test_async())
