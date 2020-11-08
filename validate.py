import json
import jsonschema
from jsonschema import validate


expr_file_path = "/Users/edwarddavies/Documents/UoM/_Modelling Data/CW2/expression7.json"
schema_file_path = "/Users/edwarddavies/Documents/UoM/_Modelling Data/CW2/Expressions.json.schema"

with open(expr_file_path, "r") as expr:
    with open(schema_file_path, "r") as schema:

        jsonData = json.load(expr)
        jsonSchema= json.load(schema)
        print(json.dumps(jsonData, indent=4))

        try:
            validate(instance=jsonData, schema=jsonSchema)
        except jsonschema.exceptions.ValidationError as err:
            print("Given JSON data is InValid")
        else:
            print("Given JSON data is Valid")
        