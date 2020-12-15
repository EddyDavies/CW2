import json
import jsonschema
from jsonschema import validate


expr_file_path = "expression11.json"
# expr_file_path = "expression_error1.json"
schema_file_path = "Expressions2.json.schema"

with open(expr_file_path, "r") as expr:
    with open(schema_file_path, "r") as schema:

        jsonData = json.load(expr)
        jsonSchema= json.load(schema)
        # print(json.dumps(jsonData, indent=4))
        print(jsonData["root"]["description"])

        try:
            validate(instance=jsonData, schema=jsonSchema)
        except jsonschema.exceptions.ValidationError as err:
            print("Given JSON data is InValid")
        else:
            print("Given JSON data is Valid")
        