#here we are checking that partner applocation is sending the data is
#converted into python data or not using json.loads() function


import json
def is_json(data):
    try:
        p_data = json.loads(data) #json to python data
        valid = True
    except ValueError:
        valid = False
    return valid
