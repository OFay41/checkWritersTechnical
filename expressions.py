from variableDef import checkFloat, list

def doMath(variableData):
    data = variableData
    for obj in list:
        data = data.replace(obj.name, obj.value)
        print(data)
    try:
        result = eval(data)
        return str(result) + "\n"
    except:
        return "please enter a valid expression\n"