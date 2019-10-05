import json
from CMS_UsingList_PureOOP import *
#Computer 1
cus=Customer()
cus.id=10
cus.name="abc10"
cus.address="xyz10"
cus.mob="100"
datainPython=5
datainPython=5.5
datainPython="Hello"
datainPython=[1,4,5,"abcd"]
datainPython=(1,4,5,"abcd")
datainPython={1:3,4:7,5:9,'a':"abcd"}
datainPython=[{"id":5,"Name":"abc5"},{"id":7,"Name":"abc7"}]
datainPython=cus


#Json Serialization Start from Here
jsonString=json.dumps(datainPython)
#Json Serialization Ends Here
print(datainPython,jsonString,type(datainPython),type(jsonString))
#Computer 2
#Json Serialization Starts from Here
datainPythonAD=json.loads(jsonString)
#Json Serialization Ends Here
print(datainPythonAD,jsonString,type(datainPythonAD),type(jsonString))