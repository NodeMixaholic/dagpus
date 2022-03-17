from numba import jit
import random

@jit(nopython=True)
def executeServerSide(code):
    codeSplit = code.split(" ")
    if (codeSplit[0] == "stringDef"):
        varDef = code.replace(codeSplit[0] + " ", "")
        varDef = varDef.replace(codeSplit[0], "")
        varDef = varDef.replace(codeSplit[1] + " ", "")
        varDef = varDef.replace(codeSplit[1], "")
        vars()[codeSplit[1]] = str(varDef)
    if (codeSplit[0] == "intDef"):
        varDef = code.replace(codeSplit[0] + " ", "")
        varDef = varDef.replace(codeSplit[0], "")
        varDef = varDef.replace(codeSplit[1] + " ", "")
        varDef = varDef.replace(codeSplit[1], "")
        vars()[codeSplit[1]] = str(varDef)
    elif (codeSplit[0] == "add"):
        nums = code.replace(codeSplit[0] + " ", "")
        nums  = nums.replace(codeSplit[0], "")
        numstrlist = nums.split(" ")
        numlist = []
        for i in numstrlist:
            numlist.append(float(i))
        return sum(numlist)
    elif (codeSplit[0] == "sub"):
        nums = code.replace(codeSplit[0] + " ", "")
        nums  = nums.replace(codeSplit[0], "")
        numstrlist = nums.split(" ")
        numlist = []
        for i in numstrlist:
            numlist.append(float(i))
        return sum(numlist) * -1



def startExecuting(code):
    ray.remote(executeServerSide(code))