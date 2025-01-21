from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from pydiator_core.serializer import JsonSerializable


class BaseRequest:
    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__


class BaseResponse(JsonSerializable):
    pass


TReq = TypeVar("TReq", bound=BaseRequest)
TRes = TypeVar("TRes", bound=Optional[BaseResponse])


class BaseHandler(ABC, Generic[TReq, TRes]):
    @abstractmethod
    async def handle(self, req: TReq) -> TRes:
        pass
