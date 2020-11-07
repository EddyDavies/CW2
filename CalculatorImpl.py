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
        
        op = getOperation(data)
        total = getDeepest(data, op, 0)

    
    return total

def getOperation(data):
    op = {}
    op["actions"] = []

    try:
        test = data["times"]
    except:
        op["times"] = False
        op["times_deeper"] = False
    else:
        op["times"] = True
        try:
            test = data["times"][0]["int"]
            test = data["times"][1]["int"]
        except:
            op["times_deeper"] = True
            op["actions"].append(["times", 2])
        else:
            op["times_deeper"] = False

    
    
    else:
        if op["times_deeper"]:
            actions.append(["times", 2])

    try:
        test = data["minus"]
    except:
        op["minus"] = False
        op["minus_deeper"] = False
    else:
        op["minus"] = True
        try:
            test = data["minus"][0]["int"]
            test = data["minus"][1]["int"]
        except:
            op["minus_deeper"] = True
            op["actions"].append(["minus", 2])
        else:
            op["minus_deeper"] = False


    try:
        test = data["plus"]
    except:
        op["plus"] = False
        op["plus_deeper"] = False
    else:
        op["plus"] = True

        success = True
        i = 0
        while success:
            try:
                test = data["plus"][i]
            except:
                success = False
            else:
                i+=1
        op["plus_count"] = i

        try:
            for j in range(i):
                test = data["plus"][j]["int"]
        except:
            op["plus_deeper"] = True
            op["actions"].append(["plus", i])
        else:
            op["plus_deeper"] = False
    
    if op["plus_deeper"] or op["minus_deeper"] or op["times_deeper"]:
        op["calculate"] = False
    else:
        op["calculate"] = True

    
    return op

def performOp(data, op, total):
    values = []
    
    try:
         test = op["times"]
    except:
        pass
    else:
        if op["times_deeper"]:
            actions.append(["times", 2])

    try:
         test = op["minus"]
    except:
        pass
    else:
        if op["minus_deeper"]:
            actions.append(["minus", 2])
            
    try:
         test = op["plus"]
    except:
        pass
    else:
        if op["plus_deeper"]:
            actions.append(["plus", op["plus_count"]])

    calculated = 0
    print("Data         " , data)
    if op["times"]:
        for i in range(2)
            try:
                values.append(data["times"][i]["int"])
            except:
                values.append(total)
            else:
                pass  
        calculated = values[0] * values[1] 

    elif op["minus"]:
        calculated = data["minus"][0]["int"] * data["minus"][0]["int"] 
        perform = "minus"

    elif op["plus"]:
        for i in range(op["plus_count"]):
            calculated += data["plus"][i]["int"] 
        # for i in range(op["plus_count"])
        perform = "plus"
    
    

    return calculated


def getDeepest(data, op, total):

    # actions = []

    # try:
    #      test = op["times"]
    # except:
    #     pass
    # else:
    #     if op["times_deeper"]:
    #         actions.append(["times", 2])

    # try:
    #      test = op["minus"]
    # except:
    #     pass
    # else:
    #     if op["minus_deeper"]:
    #         actions.append(["minus", 2])
            
    # try:
    #      test = op["plus"]
    # except:
    #     pass
    # else:
    #     if op["plus_deeper"]:
    #         actions.append(["plus", op["plus_count"]])
    
            
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
                total = performOp(data, current_op, total)
                break
            else:
                print(action[0]," go deeper")
                total = getDeepest(current_data, current_op, total)

    
    return total

# You do not need to touch anything below this line. To complete
# the assignment you need to replace the keyword "pass" in the above
# two functions with code that does the appropriate work.
if __name__=='__main__':
    expr_file_path = "/Users/edwarddavies/Documents/UoM/_Modelling Data/CW2/expression7.json"

    # expr_file_path = sys.argv[1]
    print(evaluate_expr(load_json_expr(expr_file_path)))
