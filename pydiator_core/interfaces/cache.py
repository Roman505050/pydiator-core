import enum
from abc import ABC, abstractmethod
from typing import Any


class CacheType(enum.Enum):
    NONE = 0
    DISTRIBUTED = 1


class BaseCacheable(ABC):
    def __init__(self):
        self._no_cache = False

    @abstractmethod
    def get_cache_key(self) -> str:
        pass

    @abstractmethod
    def get_cache_duration(self) -> int:
        pass

    @abstractmethod
    def get_cache_type(self) -> CacheType:
        pass

    def set_no_cache(self) -> None:
        self._no_cache = True

    def is_no_cache(self) -> bool:
        if hasattr(self, "_no_cache"):
            return self._no_cache
        return False


class BaseCacheProvider(ABC):
    @abstractmethod
    def add(self, key: str, value: Any, expire: int) -> None:
        pass

    @abstractmethod
    def get(self, key: str) -> Any:
        pass

    @abstractmethod
    def exist(self, key: str) -> bool:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass

    @abstractmethod
    def check_connection(self) -> bool:
        pass
