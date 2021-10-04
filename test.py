class variables: 
    def __init__(self, name, value): 
        self.name = name 
        self.value = value

list = []
list.append(variables("myVar", "123"))
data = "5 + 5"
for obj in list:
    data = data.replace(obj.name, obj.value)
try:    
    print(eval(data))
except:
    print ("oops")