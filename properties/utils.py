from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)


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


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    # Get the underlying redis client
    client = cache.client.get_client()

    info = client.info()  # fetch all Redis INFO stats
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics