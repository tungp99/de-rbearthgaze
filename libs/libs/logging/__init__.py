__all__ = ["Logging"]

import logging


class Logging:
    def __init__(self, name: str = None) -> None:
        self._logger = logging.getLogger(name if name is not None else f"{self.__class__.__name__}")

    @property
    def logger(self):
        """readonly property"""
        return self._logger
