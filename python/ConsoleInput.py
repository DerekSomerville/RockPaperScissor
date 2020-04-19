from Input import Input

class ConsoleInput(Input):

    def getInputString(self, request):
        return input(request)

    def getInputInt(self, request):
        return int(self.getInputString(request))
