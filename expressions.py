from variableDef import checkFloat, list

def doMath(variableData):
    data = variableData
    #replaces variables in the expression to their value
    for obj in list:
        data = data.replace(obj.name, obj.value)
        print(data)
    try:
        #runs the equation if error is thown it will alert the user
        result = eval(data)
        return str(result) + "\n"
    except:
        return "please enter a valid expression or command\n"