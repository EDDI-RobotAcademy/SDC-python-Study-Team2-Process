import abc
from dataclasses import dataclass


@dataclass
class ApplicationService(abc.ABC):

    @abc.abstractmethod
    def applicationQuit(self, *args, **kwargs):
        pass
