import json
json_str = '{"name":"yuan","age":18}'
student = json.loads(json_str)
print(type(student))