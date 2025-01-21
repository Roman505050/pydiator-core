from typing import Dict, List, Type

from pydiator_core.interfaces import (
    BaseHandler,
    BaseMediatrContainer,
    BaseNotification,
    BaseNotificationHandler,
    BasePipeline,
    BaseRequest,
)


class MediatrContainer(BaseMediatrContainer):

    def __init__(self):
        self.__requests: dict[str, BaseHandler] = {}
        self.__notifications: dict[str, List[BaseNotificationHandler]] = {}
        self.__pipelines: List[BasePipeline] = []
        self.__base_request_get_class_method_name = (
            BaseRequest.get_class_name.__name__
        )
        self.__base_notification_get_class_method_name = (
            BaseNotification.get_class_name.__name__
        )

    def register_request(self, req: Type[BaseRequest], handler: BaseHandler):
        if not isinstance(handler, BaseHandler):
            return

        if hasattr(
            req, self.__base_request_get_class_method_name
        ) and callable(
            getattr(req, self.__base_request_get_class_method_name)
        ):
            req_type = getattr(
                req, self.__base_request_get_class_method_name
            )()
            self.__requests[req_type] = handler

    def register_pipeline(self, pipeline: BasePipeline) -> None:
        self.__pipelines.append(pipeline)

    def register_notification(
        self,
        notification: type[BaseNotification],
        handlers: List[BaseNotificationHandler],
    ) -> None:
        attr = getattr(
            notification, self.__base_notification_get_class_method_name, None
        )
        if attr is not None and callable(attr):
            notification_type = attr()
            self.__notifications[notification_type] = handlers

    def get_requests(self) -> Dict[str, BaseHandler]:
        return self.__requests

    def get_notifications(self) -> Dict[str, List[BaseNotificationHandler]]:
        return self.__notifications

    def get_pipelines(self) -> List[BasePipeline]:
        return self.__pipelines

    def prepare_pipes(self, pipeline: BasePipeline) -> None:
        self.register_pipeline(pipeline)
        pipelines_length = len(self.__pipelines)
        if pipelines_length == 1:
            return

        for i in range(pipelines_length - 1, -1, -1):
            if 0 == i:
                break
            self.__pipelines[i - 1].set_next(self.__pipelines[i])
