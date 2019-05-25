import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
import json

def get_resource(id=None):


    data = {}
    if id is not None:

        data = {
        'id':id
        }
    resp = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    # print(type(resp))
    print(resp.json())

# get_resource()
# get_resource(30)

def create_resource():
    new_std = {
    'name':'dhoni',
    'rollno':8,
    'marks':35
    }
    resp = requests.post(BASE_URL+ENDPOINT,data= json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())
# create_resource()

def update_resource(id=None):
    new_std={
    'id':id,
    'name':'sakshi',
    'rollno':10,
    'marks':35
    }
    #sending post request in the form of p_dict and than convert it into json
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())

# update_resource(1)

def delete_resource(id=None):

    data = {
    'id':id,
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))

    print(resp.status_code)
    print(resp.json())
delete_resource()
