from django.shortcuts import render

# Create your views here.

#Session 15









# withoutrest2













#Session 14

#Go to serializer.py for ModelSerializer
# using django-drf we can write simple view
#DRF class provide that class name =

# 1-->APIView()  --> its like FBV complete control on logic clear flow
# 2-->ViewSet()  --> its like CBV so its complicated because we dont have command on all code

#------------------------------------APIView---------------->
#APIView is child class of View
#get(),post(),put(),etc
#we have to write code explicilitly ..complete control over the logic
#clear excecution flow
# complex operation like werking with multiple data source
#calling 3rd party apis
#we have to map views to urls mannually

#--------------------------ViewSet------------------------->
#list(),create(),retrieve(),update(),partial_update(),destroy()
#developing very simple APIs this used
#like CRUD API
#for complex APIView
#here router concept is for urls





# from testapp.models import Employee
# from django.views.generic import View
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from testapp.serializers import EmployeeSerializer
# from django.http import HttpResponse
#
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
#
#
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeCRUDCBV(View):
#     #partner application sending request to get record first take it using request.body
#     def get(self,request,*args,**kwargs):
#         json_data = request.body
#         #convert json_data into stream
#         stream = io.BytesIO(json_data)
#         #now convert into p_data
#         p_data = JSONParser().parse(stream)
#         #now whatever partner applciation is asking for the get request using id or all
#         id = p_data.get('id',None)  #if id is there than give  id if not than # None
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             #now this employee data i have to send to the partner application as json form
#             serializer = EmployeeSerializer(emp)  #converting in p_data
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         #if id is None than we have to send all data
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     #for post method we have to override create() method inside serializer
#     #in serializer.py
#     def post(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         #p_data to db supported data Deserialization
#         serializer = EmployeeSerializer(data = p_data)
#         if serializer.is_valid():
#             serializer.save()    #internally its called create method which has written in serializer create method
#             msg = {'msg': 'resouce create'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     # for put method i have to provide every field if i did not give any field it will give errors
#     def put(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         id = p_data.get('id')
#         emp = Employee.objects.get(id=id)
#         serializer = EmployeeSerializer(emp,data=p_data,partial=True)  #here emp update with data = p_data
#         #here it will checck through serializer.py that validate_esal is true or not
#         if serializer.is_valid():
#             serializer.save()  #internally called update method in serializer.py
#             msg = {'msg': 'resouce update'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     #delete can be handle without serializer
#     def delete(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         id = p_data.get('id')
#         emp = Employee.objects.get(id=id)
#         emp.delete()
#         msg = {'msg': 'delete succefully '}
#         json_data = JSONRenderer().render(msg)
#         return HttpResponse(json_data,content_type='application/json')
#
#




























# #Session 13
# from testapp.models import Employee
# from django.views.generic import View
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from testapp.serializers import EmployeeSerializer
# from django.http import HttpResponse
#
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
#
#
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeCRUDCBV(View):
#     #partner application sending request to get record first take it using request.body
#     def get(self,request,*args,**kwargs):
#         json_data = request.body
#         #convert json_data into stream
#         stream = io.BytesIO(json_data)
#         #now convert into p_data
#         p_data = JSONParser().parse(stream)
#         #now whatever partner applciation is asking for the get request using id or all
#         id = p_data.get('id',None)  #if id is there than give  id if not than # None
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             #now this employee data i have to send to the partner application as json form
#             serializer = EmployeeSerializer(emp)  #converting in p_data
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         #if id is None than we have to send all data
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     #for post method we have to override create() method inside serializer
#     #in serializer.py
#     def post(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         #p_data to db supported data Deserialization
#         serializer = EmployeeSerializer(data = p_data)
#         if serializer.is_valid():
#             serializer.save()    #internally its called create method which has written in serializer create method
#             msg = {'msg': 'resouce create'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     # for put method i have to provide every field if i did not give any field it will give errors
#     def put(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         id = p_data.get('id')
#         emp = Employee.objects.get(id=id)
#         serializer = EmployeeSerializer(emp,data=p_data,partial=True)  #here emp update with data = p_data
#         #here it will checck through serializer.py that validate_esal is true or not
#         if serializer.is_valid():
#             serializer.save()  #internally called update method in serializer.py
#             msg = {'msg': 'resouce update'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     #delete can be handle without serializer
#     def delete(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         id = p_data.get('id')
#         emp = Employee.objects.get(id=id)
#         emp.delete()
#         msg = {'msg': 'delete succefully '}
#         json_data = JSONRenderer().render(msg)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#
# #-------------------Now 3rd part Is validation--------------------
# #validation by using serializer
# #1-->field level validation    --> only one particular field
# #2--> object level validation  --> whole class or mutliple field
# #3--> by using  validators     -->
#
# #1--> field level validation -->clean_esal() or clean() in django
# # for serializer validate_fieldname() in serializer.py
#
#
# #2--> for objcet level method--> validate() in serializer.py
# #Object level validation like password and re enter password
#
# #3->inbuild validators  -->serializer.CharField
# # priority level of validators -->inbuild than object than field
#












#Session 10 DRF -->12

#Serializer -->converting one form to another form but here its done 3 activity
#1.Serialization
#2.Deserialization
#3.validation
#DRF  only access forms and modelform only


#serialization:  Go to models and than serializers.py
# from testapp.models import Employee
# from django.views.generic import View
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from testapp.serializers import EmployeeSerializer
# from django.http import HttpResponse
#
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
#
#
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeCRUDCBV(View):
#     #partner application sending request to get record first take it using request.body
#     def get(self,request,*args,**kwargs):
#         json_data = request.body
#         #convert json_data into stream
#         stream = io.BytesIO(json_data)
#         #now convert into p_data
#         p_data = JSONParser().parse(stream)
#         #now whatever partner applciation is asking for the get request using id or all
#         id = p_data.get('id',None)  #if id is there than give  id if not than # None
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             #now this employee data i have to send to the partner application as json form
#             serializer = EmployeeSerializer(emp)  #converting in p_data
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         #if id is None than we have to send all data
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     #for post method we have to override create() method inside serializer
#     #in serializer.py
#     def post(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         p_data = JSONParser().parse(stream)
#
#         #p_data to db supported data Deserialization
#         serializer = EmployeeSerializer(data = p_data)
#         if serializer.is_valid():
#             serializer.save()    #internally its called create method which has written in serializer create method
#             msg = {'msg': 'resouce create'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
