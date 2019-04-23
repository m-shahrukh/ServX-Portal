import json
 
json_data =""" {
  "User" : {
    "03230494883" : {
      "Name" : "Shahrukh",
      "Password" : "123"
    },
    "03361424139" : {
      "Name" : "Mubeen",
      "Password" : "1234",
      "email" : "",
      "vehicle" : {
        "led 1456" : {
          "vmake" : "Suzuki",
          "vmodel" : "Cultus",
          "vyear" : "2000"
        },
        "led9723" : {
          "vmake" : "Honda",
          "vmodel" : "Civic",
          "vyear" : "2007"
        },
        "lsd 112233" : {
          "vmake" : "Suzuki",
          "vmodel" : "Select Model",
          "vyear" : "2017"
        }
      }
    }
  },
  "requestID" : "0",
  "requests" : {
    "03361424139" : [ {
      "date" : "12-12-12",
      "status" : "confirmed",
      "time" : "17:00"
    } ]
  }
}"""

python_obj = json.loads(json_data)

a=python_obj["User"]["03230494883"]["Name"]
print(a)

print python_obj["requests"]


numbers=[]
for Users in python_obj["User"]:
    numbers.append(Users)

print(numbers)

if '03361424139' in numbers:
	print("dd")