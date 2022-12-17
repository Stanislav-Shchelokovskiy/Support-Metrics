from toolbox.cache.cache_object import CacheObject


class ServerCache:

    def __init__(self) -> None:
        self.stat_app_state = CacheObject('stat_app_state', expire=None)
