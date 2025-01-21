from abc import ABC, abstractmethod
from typing import Dict, List, Type

from pydiator_core.interfaces import (
    BaseHandler,
    BaseNotification,
    BaseNotificationHandler,
    BasePipeline,
    BaseRequest,
    TReq,
    TRes,
)


class BaseMediatr(ABC):

    @abstractmethod
    async def send(self, req: TReq) -> TRes:
        pass

    @abstractmethod
    async def publish(
        self, notification: BaseNotification, throw_exception: bool = False
    ):
        pass


class BaseMediatrContainer(ABC):

    @abstractmethod
    def register_request(
        self, req: Type[BaseRequest], handler: BaseHandler
    ) -> None:
        pass

    @abstractmethod
    def register_pipeline(self, pipeline: BasePipeline) -> None:
        pass

    @abstractmethod
    def register_notification(
        self,
        notification: Type[BaseNotification],
        handlers: List[BaseNotificationHandler],
    ) -> None:
        pass

    @abstractmethod
    def get_requests(self) -> Dict[str, BaseHandler]:
        pass

    @abstractmethod
    def get_notifications(self) -> Dict[str, List[BaseNotificationHandler]]:
        pass

    @abstractmethod
    def get_pipelines(self) -> List[BasePipeline]:
        pass

    @abstractmethod
    def prepare_pipes(self, pipeline: BasePipeline) -> None:
        pass
