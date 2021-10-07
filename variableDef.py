#creates a variable object that has a name and value so we can add it to list
class variables: 
    def __init__(self, name, value): 
        self.name = name 
        self.value = value

#checks to see if a value is a valid floating point number
def checkFloat(potentialFloat):
    try:
        float(potentialFloat)
        return True
    except ValueError:
        return False

#list of variables and associated value
list = []

def variableAssign(variableData):
    check = True
    #checks to see if their are spaces in the variable name (can be better) and formats data
    if variableData.find(" ") == variableData.find('=') - 1 or variableData.find(" ") == -1:
        data2 = variableData.replace(" ", "")
        x = data2.split('=')
        #checks if value of variable is valid
        if checkFloat(x[1]):
            #if the variable already exists it will reassign value if not it will add the variable to the list
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
