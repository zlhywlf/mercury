from abc import ABC
from typing import override
from mercury.core.Controller import Controller
from mercury.core.Application import Application


class BaseRdsController(Controller, ABC):
    """Remote Data Services"""

    @classmethod
    @override
    def setup(cls, application: Application) -> None:
        application.add_route(cls.path(), cls)
