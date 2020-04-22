from Input import Input
from random import randint

class InputRandom(Input):

    def getInputString(self, request):
        return getInputInt

    def getInputInt(self, request):
        return randint(0, 2)
