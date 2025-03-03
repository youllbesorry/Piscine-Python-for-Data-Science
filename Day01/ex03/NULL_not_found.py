def NULL_not_found(object: any) -> int:
    type_obj = type(object)
    if (object == None):
        print(f"Nothing: {object} {type_obj}")
    elif (type_obj == float and str(object) == "nan"):
        print(f"Cheese : {object} {type_obj}")
    elif (object == 0):
        print(f"Zero: {object} {type_obj}")
    elif (object == ''):
        print(f"Empty:  {object} {type_obj}")
    elif (object == False):
        print(f"Fake: {object} {type_obj}")
    else:
        print("Type not found")
        return (1)
    return (0)