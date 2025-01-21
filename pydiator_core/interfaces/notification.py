from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class BaseNotification:
    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__


_TNotification = TypeVar("_TNotification", bound=BaseNotification)


class BaseNotificationHandler(ABC, Generic[_TNotification]):
    @abstractmethod
    async def handle(self, notification: _TNotification) -> None:
        pass
