class variables: 
    def __init__(self, name, value): 
        self.name = name 
        self.value = value

def checkFloat(potentialFloat):
    try:
        float(potentialFloat)
        return True
    except ValueError:
        return False

list = []

def variableAssign(variableData):
    check = True
    if variableData.find(" ") == variableData.find('=') - 1:
        data2 = variableData.replace(" ", "")
        x = data2.split('=')
        if checkFloat(x[1]):
            for obj in list:
                if obj.name == x[0]:
                    obj.value = x[1]
                    check = False
            if check:
                list.append( variables(x[0], x[1]) )
            check = True
            return x[0] + " has been set to " + x[1] + "\n"
        else:
            return "variables must be a valid foating point number\n"
        for obj in list:
            print(obj.value)
    else:
        return "variables cannot have spaces\n"
