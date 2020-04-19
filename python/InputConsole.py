from Input import Input

class InputConsole(Input):

    def getInputString(self, request):
        return input(request)

    def getInputInt(self, request):
        return int(self.getInputString(request))
