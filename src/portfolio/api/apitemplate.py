from datetime import datetime, timezone

class ApiTemplate:
    def __init__(self):
        self._CACHE_TIME: int = 900 # 15 minutes * 60 seconds

        self._last_cache_time: int = 0

    def _should_refresh_cache(self) -> bool:
        current_time: int = int(datetime.now(timezone.utc).timestamp())

        cache_time: int = self._last_cache_time + self._CACHE_TIME

        if (current_time < cache_time):
            return False

        # Encourage cache refresh when it should
        self._last_cache_time = current_time
        return True