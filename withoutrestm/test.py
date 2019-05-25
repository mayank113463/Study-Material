import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
import json
#Session 9
#here i want if i pass the id than it will give id record
#if i dont than it should give whole record
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
    'ename':'villen',
    'esal':5450,
    'eadd':'shivkuti'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data= json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
# create_resource()

def update_resource(id=None):
    new_emp={
    'id':id,
    'eadd':'Delhi'
    }
    #sending post request in the form of p_dict and than convert it into json
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

# update_resource()

def delete_resource(id=None):

    data = {
    'id':id,
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))

    print(resp.status_code)
    print(resp.json())
# delete_resource()










# #Session 8
# import json
# def update_resource(id):
#     new_emp={
#     'eno':100,
#     'ename':'villen_good',
#     'esal':500000,
#     'eadd':'allahabad'
#     }
#     #sending post request in the form of p_dict and than convert it into json
#     resp = requests.put(BASE_URL+ENDPOINT+str(id)+'/',data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# # update_resource(1)
#
# def delete_resource(id):
#     resp = requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(5)
#














#Session 7
#create employee data or post
# import json
# def create_resource():
#     new_emp={
#     'eno':100,
#     'ename':'villen',
#     'esal':50000,
#     'eadd':'shivkuti'
#     }
#     #sending post request in the form of p_dict and than convert it into json
#     resp = requests.post(BASE_URL+ENDPOINT,data= json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
#
#



#Session 6 3rd part
#handle exception from partner application the error of DoesNotExist of Employee
# print employee data using id
# def get_resource(id):
#         resp = requests.get(BASE_URL+ENDPOINT+id+'/')
#         # if resp.status_code in range(200,300): #we can use this line or below line alos
#         if resp.status_code == requests.codes.ok:
#             print(resp.json())
#         else:
#             print('something goes wrong')
#         #here response (resp would be in form of respinse object so it has to convert into dict python form)
#         #using resp.json()...json always return in the form of dict
#
#         # print(type(resp))
#
# id = input("enter id :  ")
# get_resource(id)
#






# print("hi")
# print employee data using id
# def get_resource(id):
#         resp = requests.get(BASE_URL+ENDPOINT+id+'/')
#         #here response (resp would be in form of respinse object so it has to convert into dict python form)
#         #using resp.json()...json always return in the form of dict
#         print(resp.status_code)
#         # print(type(resp))
#         print(resp.json())
# id = input("enter id :  ")
# get_resource(id)
#
#
#
# #print all data of employee
# def get_all():
#         resp = requests.get(BASE_URL+ENDPOINT)
#         #here response (resp would be in form of respinse object so it has to convert into dict python form)
#         #using resp.json()...json always return in the form of dict
#         print(resp.status_code)
#         # print(type(resp))  #<class 'requests.models.Response'>
#         print(type(resp.json())) #--> <class 'list'>
#         print(resp.json())
# get_all()
