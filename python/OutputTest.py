from Output import Output

class OutputTest(Output):

    outputlist = []

    def setOutputList(self,outputList):
        self.outputlist = outputList

    def print(self, request):
        self.outputlist.append(request)
