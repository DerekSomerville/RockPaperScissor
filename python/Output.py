from abc import ABC, abstractmethod

class Output(ABC):

    @abstractmethod
    def print(self, request):
        pass
