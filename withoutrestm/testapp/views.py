from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
# Create your views here.


#Session 9

        #here is a problem that if enpoint is same like for all
        #get http://127.0.0.1:8000/api/1
        #create http://127.0.0.1:8000/api/
        #update http://127.0.0.1:8000/api/1
        #delete http://127.0.0.1:8000/api/1
        #so its same for all endpoint




from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_oject_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def post(self,request,*args,**kwargs):
            data = request.body
            valid_json = is_json(data)
            if not valid_json:
                json_data = json.dumps({'msg':'please send valid json only'})
                return self.render_to_http_response(json_data,status=400)
            empdata = json.loads(data)
            form = EmployeeForm(empdata)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'resource created successfully'})
                return self.render_to_http_response(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data,status=400)


    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None) # if id is available than return id if not return None
        #if id is provided by client than this part
        if id is not None:
            emp = self.get_oject_by_id(id)
            #if employee is not available
            if emp is None:
                json_data = json.dumps({'msg':'record not available'})
                return self.render_to_http_response(json_data,status=400)
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        #if id is not provided by client
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)


    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None) # if id is available than return id if not return None

        if id is None:
            json_data = json.dumps({'msg':'to prtform data id is mendatory '})
            return self.render_to_http_response(json_data,status=400)

        emp = self.get_oject_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'id is not available'})
            return self.render_to_http_response(json_data,status=400)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename': emp.ename,
        'esal':emp.esal,
        'eadd':emp.eadd,
        }
        original_data.update(provided_data)

        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None) # if id is available than return id if not return None
        #if id is provided by client than this part
        if id is not None:
            emp = self.get_oject_by_id(id)
            #if employee is not available
            if emp is None:
                json_data = json.dumps({'msg':'record not available'})
                return self.render_to_http_response(json_data,status=400)

            status,deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'resource deleted successfully'})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({'msg': 'unable to delete please try again'})
            return self.render_to_http_response(json_data)

        json_data = json.dumps({'msg':'to perfomr deletion provide id'})
        return self.render_to_http_response(json_data,status=400)














#Session 8
#
#
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from testapp.utils import is_json
# from testapp.forms import EmployeeForm
#
#
# @method_decorator(csrf_exempt,name='dispatch') #for class based views here if name is dispatch than its aaplicable for all request like post put etc
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get_oject_by_id(self,id):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp = None
#         return emp
#
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#
#             json_data = json.dumps({'msg': 'the requested resoure not available'})
#             # return HttpResponse(json_data,content_type='application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data = self.serialize([emp,])
#             # return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)
#
#     def put(self,request,id,*args,**kwargs):
#         # try:
#         #     emp = Employee.objects.get(id=id)
#         # except Employee.DoesNotExist:
#         #     emp = None
#         # insted of putting again and again this same method i have to write it in a method above the class name as get_oject_by_id
#         emp = self.get_oject_by_id(id)
#         if emp is None:
#             json_data = json.dumps({'msg': 'Not possible updation of unmatchng record'})
#             return self.render_to_http_response(json_data,status=404)
#         data = request.body
#         valid_json = is_json(data)
#         if not valid_json:
#             json_data = json.dumps({'msg':'please provide valid json data for put method'})
#             return self.render_to_http_response(json_data,status=400)
#         provided_data = json.loads(data)
#         #now the required updation comes into provided_data so i have to change in the original data
#         original_data = {
#         'eno':emp.eno,
#         'ename': emp.ename,
#         'esal':emp.esal,
#         'eadd':emp.eadd,
#         }
#
#         # #original_data = {
#         # 'eno':45,
#         # 'ename':'bhai',
#         # 'esal':100000,
#         # 'eadd':varansi,
#         # }
#         # provided_data = {
#         # 'eno':100,
#         # 'ename':'villen_good',
#         # 'esal':500000,
#         # 'eadd':'allahabad'
#         #
#         # }
#         #here updation through update keyword in python what we want to update
#         original_data.update(provided_data)
#         # print(original_data)
#         #now i have to add it intoo the database but when i am submitting forms
#
#         # form = EmployeeForm(original_data)
#         # if form.is_valid():
#         #     form.save(commit=True)
#         #     json_data = json.dumps({'msg': 'resource updated successfully'})
#         #     return self.render_to_http_response(json_data)
#         # if form.errors:
#         #     json_data = json.dumps(form.errors)
#         #     return self.render_to_http_response(json_data,status=400)
#
#         #its creating new record isntead of updating
#         #so i have to write in arugment  instance of that employee objcet above form
#
#         form = EmployeeForm(original_data,instance=emp)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data = json.dumps({'msg': 'resource updated successfully'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data = json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#
#         #post -->EmployeeForm(original_data)
#         #put  --> EmployeeForm(original_data,instance=emp)
#     def delete(self,request,id,*args,**kwargs):
#         emp = self.get_oject_by_id(id)
#         if emp is None:
#             json_data = json.dumps({'msg': 'Not possible updation of unmatchng record'})
#             return self.render_to_http_response(json_data,status=404)
#         # t= emp.delete()
#         # print(t)   #(1, {'testapp.Employee': 1}) its print tuples like status and which record deleted
#         # json_data = json.dumps({'msg': 'resource deleted successfully'})
#         # return self.render_to_http_response(json_data)
#         status,deleted_item = emp.delete()  #storing tuples in tuples into tuples form
#         if status == 1:
#             json_data = json.dumps({'msg': 'resource deleted successfully'})
#             return self.render_to_http_response(json_data)
#         json_data = json.dumps({'msg': 'unable to delete please try again'})
#         return self.render_to_http_response(json_data)
#
#
#
#
# @method_decorator(csrf_exempt,name='dispatch')  #its disabling the csrf token for class levele
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get(self,request,*args,**kwargs):
#         qs = Employee.objects.all()
#         json_data = self.serialize(qs)  #self.classmethod calling
#         return HttpResponse(json_data,content_type='application/json',status=200)
#
#
#
#     def post(self,request,*args,**kwargs):
#         data = request.body
#         valid_json = is_json(data)
#         if not valid_json:
#             json_data = json.dumps({'msg':'please send valid json only'})
#             return self.render_to_http_response(json_data,status=400)
#         empdata = json.loads(data)
#         form = EmployeeForm(empdata)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data = json.dumps({'msg': 'resource created successfully'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data = json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#
#
#

























#Session 7
#you can dump data using python manage.py dumpdata app.models --indent 4
#or xml format in cmd python manage.py dumpdata testapp.Employee --format xml --indent 10

#i can save this file in file also  python manage.py dumpdata testapp.Employee --format xml > emp.xml --indent 10   -->into emp.xml
# python manage.py dumpdata testapp.Employee > emp.json --indent 10


#learn post record
#disable csrf is  for post level so we have to secure out post method using
#1-->Method or function level -->@csrf_exempt on the top of method or function
#2--> Class level  -># @method_decorator(csrf_exempt,name='dispatch') #for class based views here if name is dispatch than its aaplicable for all request like post put etc

#for method level is csrf_exempt
#now check the post data is python data or not for that we check using utils.py


# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from testapp.utils import is_json
# from testapp.forms import EmployeeForm
#
#
# @method_decorator(csrf_exempt,name='dispatch') #for class based views here if name is dispatch than its aaplicable for all request like post put etc
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#
#             json_data = json.dumps({'msg': 'the requested resoure not available'})
#             # return HttpResponse(json_data,content_type='application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data = self.serialize([emp,])
#             # return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)
#
#
#
# @method_decorator(csrf_exempt,name='dispatch')  #its disabling the csrf token for class levele
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get(self,request,*args,**kwargs):
#         qs = Employee.objects.all()
#         json_data = self.serialize(qs)  #self.classmethod calling
#         return HttpResponse(json_data,content_type='application/json',status=200)
#
#     def post(self,request,*args,**kwargs):
#         #here i have to receive the data in the form of request.body
#         data = request.body
#         valid_json = is_json(data)
#         if not valid_json:
#             json_data = json.dumps({'msg':'please send valid json only'})
#             return self.render_to_http_response(json_data,status=400)
#         #if its post data so we have to save the data in database using form
#         #whatever data is provided by partner application highly recommended that we should use ModelForm to store in the database
#         #using forms.py now whatever the data is coming that would be in the form of json so convert it into p_data
#         empdata = json.loads(data)
#         form = EmployeeForm(empdata)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data = json.dumps({'msg': 'resource created successfully'})
#             return self.render_to_http_response(json_data)
#
#         if form.errors:
#             #in forms.py if validation is fail than this part will execute
#             #here form.errors is already dictionary
#             json_data = json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#



        # json_data = json.dumps({'msg': 'this is from post method'})
        # return self.render_to_http_response(json_data)



























#
# #Session 6 3rd part
# #now if i dont have id=300 it will give error like
# #   ***** Employee matching query does not exist. ***
# #So we have to handle that exception
# #add status code for success_code
# #return HttpResponse using multiple times so we can use httpresponse mixiin using mixins method
# from testapp.mixins import SerializeMixin,HttpResponseMixin
#
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get(self,request,*args,**kwargs):
#         qs = Employee.objects.all()
#         json_data = self.serialize(qs)  #self.classmethod calling
#         return HttpResponse(json_data,content_type='application/json',status=200)
#
#
#
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#
#             json_data = json.dumps({'msg': 'the requested resoure not available'})
#             # return HttpResponse(json_data,content_type='application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data = self.serialize([emp,])
#             # return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)
#
#
#
#
#
#
#
#
#










#Session 6 2nd part
#here in last session i am using that part to extract fields objects from the python dict but when i am opening in browser it is showing same as previous like extra information
#[{"model": "testapp.employee", "pk": 2, "fields": {"eno": 2, "ename": "sunny", "eadd": "1511"}}]
#so for browser result show same i have to create a mixin class for that so that we can use that where i want to user that


# from testapp.mixins import SerializeMixin
#
# class EmployeeListCBV(SerializeMixin,View):
#
#     def get(self,request,*args,**kwargs):
#         qs = Employee.objects.all()
#         json_data = self.serialize(qs)  #self.classmethod calling
#         return HttpResponse(json_data,content_type='application/json')
#
#
#
# class EmployeeDetailCBV(SerializeMixin,View):
#
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#
#         json_data = self.serialize([emp,])
#         return HttpResponse(json_data,content_type='application/json')
#
#
#
















#Session 6

# class EmployeeListCBV(View):
#     #fetching all records from employee data
#     def get(self,request,*args,**kwargs):
#         #only next line is change
#         qs = Employee.objects.all()
#         json_data = serialize('json',qs,fields=('eno','ename'))
#         #we are using serialize so we have to convert the objects with exyta information like model and nmodel name so after that we have to convert it into python dict so we can exxtract the required fields
#         #so converting into python dict using loads
#         # print(type(json_data))
#         #<class 'str'>
#         #next line convert json to python dictionary to extract the title fromm this
#         p_data = json.loads(json_data)
#
#         # print(pdict) #--> on server console it will print list of dict object
#         #[{'model': 'testapp.employee', 'pk': 1, 'fields': {'eno': 1, 'ename': 'mayank', 'esal': 1234.0, 'eadd': '1234'}}, {'model': 'testapp.employee', 'pk': 2, 'fields': {'eno': 2, 'ename': 'sunny', 'esal': 12348545.0, 'eadd': '1511'}}]
#         # i want only fiels of fields of employee
#         final_list = []
#         for eachobj in p_data:
#             empt_data = eachobj['fields'] #add only fiels dict
#             final_list.append(empt_data)
#         #this final_list is python data so we have to convert it into json
#         json_data = json.dumps(final_list)
#         # print(type(final_list))
#         # <class 'list'> dumps encoding to json objects
#         # print(type(json_data))
#         #<class 'str'>
#         # print(final_list)  #python dict
#         # print(json_data)  #json_data
#         return HttpResponse(json_data,content_type='application/json')
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Session 5
#
#
# #serialization python object into json_data
# #1--> by using python inbuilt modules json   -->json.dumps(data)
# #2--> by using django serialize()  --> from django.core.serializers import serialize
# #3--> by using django.core.serializers import serialize
#
#
# class EmployeeDetailCBV(View):
#
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#         # emp_data = {
#         # 'eno' : emp.eno,
#         # 'ename' : emp.ename,
#         # 'esal' : emp.esal,
#         # 'eadd' : emp.eadd,
#         # }
#         #here we are trying to convert employee object-> python dict and than json this called serialization concept
#         #convert python dict object to json object called serialization
#
#         # json_data = json.dumps(emp_data)
#         # so for list of objects like Employee.objects.all() convert into json serializers (djagno inbuilt modules)
#         #serialize('json',queryset,fields)  -->where queryset is in form of list or tuples except objects
#         #fields is mention that only these fields will show to the other userapp
#         #here emp passing as list
#         #serialize take list as second argument so i convert it into list
#         json_data = serialize('json',(emp,),fields =('eno','ename','eadd'))
#         return HttpResponse(json_data,content_type='application/json')
#




#Session 4


# class EmployeeDetailCBV(View):
#
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#         #here i have to send the emp id =1 to the json format so for that we have to convert first object into dict form and than json form
#         emp_data = {
#         'eno' : emp.eno,
#         'ename' : emp.ename,
#         'esal' : emp.esal,
#         'eadd' : emp.eadd,
#         }
#         #now convert this dic to json object using json.dumps
#         json_data = json.dumps(emp_data)
#         #return the response as json format
#         return HttpResponse(json_data,content_type='application/json')
