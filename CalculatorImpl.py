import json
import sys


def evaluate_expr(parsed_expr):
    """This function takes an expression parsed from the JSON
       arithmetic expression format and returns the full evaluation.
       That is, if the JSON expresses '1+1', this function returns '2'."""
    pass

def load_json_expr(json_path):
    """This function takes a file path to a JSON file  represened
       as a string and returns a parsed form. You can presume that
       the JSON file is valid wrt the arithmetic expression format."""
    end = False

    with open(json_path, "r") as f:
        data = json.load(f)
        data = data["root"]
        
        op = {"actions": None}
        total = getDeepest(data, op, 0)

    
    return total

def getOperation(data):
    op = {}
    op["actions"] = []
    op["calculate"] = True

    try:
        test = data["times"]
    except:
        pass
    else:
        try:
            test = data["times"][0]["int"]
            test = data["times"][1]["int"]
        except:
            op["actions"].append(["times", 2, True])
            op["calculate"] = False
        else:
            op["actions"].append(["times", 2, False])

    try:
        test = data["minus"]
    except:
        pass
    else:
        try:
            test = data["minus"][0]["int"]
            test = data["minus"][1]["int"]
        except:
            op["actions"].append(["minus", 2, True])
            op["calculate"] = False
        else:
            op["actions"].append(["minus", 2, False])


    try:
        test = data["plus"]
    except:
        pass
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
            op["actions"].append(["plus", i, True])
            op["calculate"] = False
        else:
            op["actions"].append(["plus", i, False])
    
    return op

def performOperation(data, op, total):
    
    calculated = 0
    print("Data         " , data)

    for action in op["actions"]:
        first = None

        for i in range(action[1]):
            try:
                value = data[action[0]][i]["int"]
            except: 
                value = total

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

    print("                       ",op)
    print()
    print("                       ",data)
    print()
    print(calculated)

    return calculated

def getDeepest(data, op, total):
    if op["actions"] is None:
        op = getOperation(data)

    for action in op["actions"]:
        for i in range(action[1]):
            current_data = data[action[0]][i]
            current_op = getOperation(current_data)
            # print(action[0])
            # print("                       ",op)
            # print()
            # print("                       ",data)
            # print()
            if current_op["calculate"]:
                print(action[0], " calculate it")
                total = performOperation(data, current_op, total)
                break
            else:
                print(action[0]," go deeper")
                total = getDeepest(current_data, current_op, total)

    
    return total

# You do not need to touch anything below this line. To complete
# the assignment you need to replace the keyword "pass" in the above
# two functions with code that does the appropriate work.
if __name__=='__main__':
    expr_file_path = "/Users/edwarddavies/Documents/UoM/_Modelling Data/CW2/expression1.json"

    # expr_file_path = sys.argv[1]
    print(evaluate_expr(load_json_expr(expr_file_path)))
