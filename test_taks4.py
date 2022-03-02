#!/usr/bin/python3
from models.base_model import BaseModel

print("---------------------------------[4]-------------------------------------\n\n")

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
my_new_model_json = my_new_model.to_dict()
print(my_new_model_json)

print("--")
print(my_model is my_new_model)

print("------------")
d = {
    "id": "67a5de98-a043-40df-afa9-3548931e3b72",
    "created_at": "2022-03-01T22:06:49.709057",
    "updated_at": "2022-03-01T22:06:49.709223",
    "name": "My_First_Model",
    "my_number": 89,
    "__class__": "BaseModel",
}
print(len(d))
new = BaseModel(**d)
print(new)
print(type(new.created_at))
new_json = new.to_dict()
print(new_json)
