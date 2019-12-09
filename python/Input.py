from abc import ABC, abstractmethod

class Input(ABC):

    @abstractmethod
    def getInputString(self, request):
        pass
    @abstractmethod
    def getInputInt(self, request):
        pass


class ConsoleInput(Input):

    def getInputString(self, request):
        return input(request)

    def getInputInt(self, request):
        return int(getInputString(request))
