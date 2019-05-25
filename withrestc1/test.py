import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
import json


#Session 13

# for put method i have to provide every field if i did not give any field it will give errors

# def update_resource(id=None):
#     new_emp={
#     'id':id,
#     'eno':14,
#     'ename':'shraddha kapoor',
#     'esal':54500,
#     'eadd':'mumbai'
#     }
#     #sending post request in the form of p_dict and than convert it into json
#     resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# update_resource(1)


#for partial data we have to add in views.py partial = True

def update_resource(id=None):
    new_emp={
    'id':id,
    'eno':10,
    'ename':' sunny',
    'esal' : 100045
    }
    #sending post request in the form of p_dict and than convert it into json
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

update_resource(3)

def delete_resource(id=None):

    data = {
    'id':id,
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))

    print(resp.status_code)
    print(resp.json())
# delete_resource(6)






#session 10 to 12
def get_resource(id=None):   #id=None that default is None
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
# get_resource(2)


def create_resource(id =None):
    new_emp={
    'eno':140,
    'ename':'shakti kapoor',
    'esal':54500,
    'eadd':'shivkuti'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data= json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
# create_resource()
