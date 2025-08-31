from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all properties with low-level caching in Redis.
    Cache key: 'all_properties'
    Timeout: 3600 seconds (1 hour)
    """
    # Try to get from cache
    properties = cache.get("all_properties")
    if properties is None:
        # Not in cache, fetch from DB
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location"
        ))
        # Store in Redis
        cache.set("all_properties", properties, 3600)
    return properties