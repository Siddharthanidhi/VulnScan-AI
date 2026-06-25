from abc import ABC, abstractmethod


class BaseCollector(ABC):

    id = ""
    name = ""

    @abstractmethod
    def collect(self, context):
        pass