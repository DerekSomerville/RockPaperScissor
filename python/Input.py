from abc import ABC, abstractmethod

class Input(ABC):

    @abstractmethod
    def getInputString(self, request):
        pass
    @abstractmethod
    def getInputInt(self, request):
        pass



