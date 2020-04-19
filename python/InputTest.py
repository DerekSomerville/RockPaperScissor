from Input import Input

class InputConsole(Input):

    inputList = []

    def getInputString(self, request):
        return inputList.pop()

    def getInputInt(self, request):
        return int(self.getInputString(request))
