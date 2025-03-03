def all_thing_is_obj(object: any) -> int:
    type_obj = type(object)
    if (type(object) in [list, tuple, set, dict]):
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    elif (type_obj == str):
        print(f"{object} is in the kitchen : {type_obj}")
    else:
        print("Type not found")
    return 42
