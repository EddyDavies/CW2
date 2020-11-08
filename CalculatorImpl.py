import json
import sys


def evaluate_expr(parsed_expr):
    """This function takes an expression parsed from the JSON
       arithmetic expression format and returns the full evaluation.
       That is, if the JSON expresses '1+1', this function returns '2'."""

    op = {"actions": None}
    total = getDeepest(parsed_expr, op)
    
    print(parsed_expr["description"])
    return total
def load_json_expr(json_path):
    """This function takes a file path to a JSON file  represened
       as a string and returns a parsed form. You can presume that
       the JSON file is valid wrt the arithmetic expression format."""

    with open(json_path, "r") as f:
        data = json.load(f)
        data = data["root"]
    
    return data

def getDeepest(data, op):
    total = []

    if op["actions"] is None:
        # print("Action is None")
        op = getOperation(data)
        if op["calculate"]:
            # print("Calculate from None")
            total = performOperation(data, op, total)
            return total
            

    for action in op["actions"]:
        for i in range(action[1]):
            total.append(None)

        
        for i in range(action[1]):
            current_data = data[action[0]][i]
            current_op = getOperation(current_data)
            # print()
            # print("current_op")
            # print("        ", current_op)
            # print("current_data")
            # print("        ",current_data)
            # print()
            if current_op["calculate"] and not current_op["tier_up"]:
                # print("Perform ", action[0], " calculation on current")
                total[i] = performOperation(current_data, current_op, total)
            elif current_op["tier_up"]:
                # print("Perform ", action[0], " calculation on layer above.")
                total[i] = performOperation(data, op, total)
            else:
                # print("Another layer Nested inside the ", action[0])
                total[i] = getDeepest(current_data, current_op)
            
            if total[-1] is not None:
                # print("Perform ", action[0], " calculation of totals.")
                total = performOperation(data, op, total)


    return total

def getOperation(data):
    op = {"actions" : [], "calculate": True, "tier_up" : False}
    checked = 0

    try:
        test = data["times"]
    except:
        checked +=1
    else:
        try:
            test = data["times"][0]["int"]
            test = data["times"][1]["int"]
        except:
            op["actions"].append(["times", 2, {"deeper" : True}])
            op["calculate"] = False
        else:
            op["actions"].append(["times", 2, {"deeper" : False}])

    try:
        test = data["minus"]
    except:
        checked +=1
    else:
        try:
            test = data["minus"][0]["int"]
            test = data["minus"][1]["int"]
        except:
            op["actions"].append(["minus", 2, {"deeper" : True}])
            op["calculate"] = False
        else:
            op["actions"].append(["minus", 2, {"deeper" : False}])


    try:
        test = data["plus"]
    except:
        checked +=1
    else:
        success = True
        i = 0
        while success:
            try:
                test = data["plus"][i]
            except:
                success = False
            else:
                i+=1
                
        try:
            for j in range(i):
                test = data["plus"][j]["int"]
        except:
            op["actions"].append(["plus", i, {"deeper" : True}])
            op["calculate"] = False
        else:
            op["actions"].append(["plus", i, {"deeper" : False}])
    
    if checked is 3:
        op["tier_up"] = True 

    return op

def performOperation(data, op, total):

    calculated = 0
    first = None

    for action in op["actions"]:

        for i in range(action[1]):
            try:
                value = data[action[0]][i]["int"]
            except: 
                value = total[i]

            if action[0] is "plus":
                calculated += value 
            elif first is None:
                first = value
            else:
                if action[0] is "times":
                    calculated = first * value
                elif action[0] is "minus":
                    calculated = first - value
                first = None

        # print("Calculated as = ", calculated)


    return calculated


# You do not need to touch anything below this line. To complete
# the assignment you need to replace the keyword "pass" in the above
# two functions with code that does the appropriate work.
if __name__=='__main__':
    expr_file_path = sys.argv[1]
    print(evaluate_expr(load_json_expr(expr_file_path)))
