def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print (f"List : {type(object)}")
    if type(object) == tuple:
        print (f"Tuple : {type(object)}")
    if type(object) == set:
        print (f"Set : {type(object)}")
    if type(object) == dict:
        print (f"Dict : {type(object)}")
    if type(object) == str:
        print (f"{object} is in the kitchen : {type(object)}")
    else:
        print ("Type not found$")
    return 42