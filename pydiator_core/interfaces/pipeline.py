from abc import ABC, abstractmethod
from typing import Union, Optional

from pydiator_core.interfaces.handler import BaseHandler, TReq, TRes


class BasePipeline(ABC):
    _next: Optional[Union[BaseHandler, "BasePipeline"]] = None

    def next(self) -> Optional[Union[BaseHandler, "BasePipeline"]]:
        return self._next

    def set_next(
        self, handler: Optional[Union[BaseHandler, "BasePipeline"]]
    ) -> None:
        self._next = handler

    def has_next(self) -> bool:
        return self._next is not None

    @abstractmethod
    async def handle(self, req: TReq) -> TRes:
        pass
