import json
def is_json(data):
    try:
        real_data = json.loads(data)
        valid = True
    except:
        valid = False
    return valid
