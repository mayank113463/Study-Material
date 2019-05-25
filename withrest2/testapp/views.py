from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response  #python dict to json_Data
from testapp.serializer import NameSerializer
# Create your views here.

#Session 16

#--------APIView------
#present in rest_framework.views module
#method names reflect Http method get(),post(),patch(),delete()
#map views  url explicilitly
#most of bussiness logic we have to explicilitly
#length of the code is long
#api development time is long
#complette control on bussiness logic
#clear execution flow is possible
#best suitable for complex operations like using mutliple data source simuntaneouly and calling other






#---------ViewSet--------------
#present in rest_framework.viewsets module
#method names reflect database model class actions like list(),create(),update(),destroy()
#here not reuired to map views to urls explicilitly
#most of the bussiness logic Generated automatically
#length of the code less
#api development time is less
#not complete control on bussiness logic
#clear execution flow is not possible
#best suitable for developing simple api like crud interface for database

























#Session 15
#here APIView has all method inbuild that is get put create etc
#here Response class in rest_framework which convert python dict to json_Data
#browsable api here
# class TestAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         colors = ['RED','Yellow','Green','Blue']
#         return Response({'msg':'Happy pongal !','colors':colors})
#
#     def post(self,request,*args,**kwargs):
#         #for post request partner application send json_Data
#         #so we have to go for serializer.py just because of conversion
#         #here NameSerializer is reponsible to convert json_Data to pdata
#         #csrf token no need to disable internally its take care
#         serializer = NameSerializer(data = request.data)
#         if serializer.is_valid():
#             name = serializer.data.get('name')
#             msg = 'hello {} happy pongal !!'.format(name)
#             return Response({'msg':msg})
#         else:
#             return Response(serializer.errors,status=400)
#
#     def put(self,request,*args,**kwargs):
#         return Response({"msg":"from put method"})
#
#     def patch(self,request,*args,**kwargs):
#         return Response({"msg":"from patch method"})
#
#     def delete(self,request,*args,**kwargs):
#         return Response({"msg":"from delete method"})
#
#
#
#
#
#
# #--------------------ViewSet----------------------------
# #in APIView :http methods are there get ,post ,post,delete
# #for ViewSet  :method are
# #1-->list()-->to get all records
# #2--> retrieve()--> to get a specefic resource
# #3--> create() --> to create new resource
# #4--> update() --> to perform ful update
# #5--> partial_update()  --> partial update
# #6--> destroy() --> delete a resource
#
# #get() --> list(),retrieve()
# #post() --> create()
# #put()  --> update()
# #patch() -->partial_update()
# #delete() --> destroy()
#
#
#
# #-------------when ViewSet are best choice-----------------#
# #if you want to develop simple crud interface for application
# #if want very quicky
# #if not want to perform complex operations
# #if want to perform standard operations
#
#
#
# #--------------ViewSet Examples-----------#
# #go to urls.py where routers map that automatically
# #routers will help map views to url automatically
# #DRF provide one class DefaultRouter so no need to create url mannually
#
# from rest_framework.viewsets import ViewSet
#
# class TestViewSet(ViewSet):
#     def list(self,request):
#         colors = ['RED','Yellow','Green','Blue']
#         return Response({'msg':'Happy pongal !','colors':colors})
#     def create(self,request):
#         serializer = NameSerializer(data = request.data)
#         if serializer.is_valid():
#             name = serializer.data.get('name')
#             msg = 'hello {} happy pongal !!'.format(name)
#             return Response({'msg':msg})
#         else:
#             return Response(serializer.errors,status=400)
#
#
# #all 4 methods needs pk for delete update partial_update and retrieve
# #http://localhost:8000/test-view-set/1/
#     def retrieve(self,request,pk=None):
#         return Response({"msg":"from retrieve method"})
#
#     def update(self,request,pk=None):
#         return Response({"msg":"from update method"})
#
#     def partial_update(self,request,pk=None):
#         return Response({"msg":"from partial_update method"})
#
#     def destroy(self,request,pk=None):
#         return Response({"msg":"from partial_update method"})
