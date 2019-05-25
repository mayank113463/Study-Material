#Sesson 18

#mixins --> normal class meant for code resusability
#direct child class of object class
#contain only method not variable

#from rest_framework.mixins
#ListModelMixin
#CreateModelMixin
#RetrieveModelMixin
#UpdateModelMixin
#DestroyModelMixin



#1--> ListModelMixin
#to implement list operation(get method handler)
#list(request,*args,**kwargs)


#2-->CreateModelMixin
#create method
#create(request,*args,**kwargs)


#3-->UpdateModelMixin
#update(request,*args,**kwargs)

#4--> RetrieveModelMixin
#retrieve(request,*args,**kwargs)

#5-->#DestroyModelMixin
#destroy(request,*args,**kwargs)

from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

# class EmployeeListCreateModelMixins(generics.ListAPIView):

#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


#     #here ListAPIView can perfom only listing and i didnt use any mixins
#     #so its giving only list of all employee not create  but i want to perfom
#     #the create also employee with same class i can add mixins
#      #and add the method of CreateModelMixin that is post()

class EmployeeListCreateModelMixins(mixins.CreateModelMixin,generics.ListAPIView):

#--------------------CreateModelMixin internall-------------------#
#### # def create(self, request, *args, **kwargs):
 ####        serializer = self.get_serializer(data=request.data)
######        serializer.is_valid(raise_exception=True)
 ####        self.perform_create(serializer)
 ####        headers = self.get_success_headers(serializer.data)
 ####        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    #CreateModelMixin internally called create method below menthion
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class EmployeeRetrieveUpdateDestroyModelMixins(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.parttial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(self,request,*args,**kwargs)



#-----------whenever APIView if you want to implement than use http method
#------but for Viewset implement database related method we have to implement

























#
#
#
# from django.shortcuts import render
# from rest_framework.views import APIView
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer
# from rest_framework.response import Response
#
#
#
#
# # Create your views here.
# #
# #Session 16  & 17
#
# # class EmployeeListAPIView(APIView):
# #     def get(self,request,format=None):
# #         qs = Employee.objects.all()
# #         #here serializer is converting json to pdata
# #         serializer = EmployeeSerializer(qs,many=True)
# #         #serializer.data is python dictionary
# #         return Response(serializer.data)
# #         #now we have to convert into json for that i used in last class renderer but here Response will take care of everything
# #         #so it will convert into json also
#
#
#
#
#
#
# #for list representation you can use ListAPIView for show list
# #this class is present inside rest_framework.generic module
# #here we dont have to define get method
# from rest_framework.generics import ListAPIView,DestroyAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
#
# class EmployeeListAPIView(ListAPIView):
#     #here queryset and serializer_class is predefine keyword in ListAPIView
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
# #---------for search operation--------#
# #we have to override get_queryset() method to implement serch # operation
# #whenever  In ListAPIView method Employee.objects.all is calling internally get_queryset return considered as queryset
# #if localhost:8000/api/?ename=sunny
# #after the ? in url all string considered as queryset
#
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#             return qs
#
# #createAPIView for post method
#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     #a particular employee key ..for that primary key in urls.py
#     #its always expecting pk in urls.py if you give any other id than it will not work
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# #----------error ------------------------------------#
# # Expected view EmployeeRetrieveAPIView to be called with a URL keyword argument named "pk". Fix your URL conf, or set the `.lookup_field` attribute on the view correctly.
#
#     #so i can use lookup_field for id in urls.py
#     lookup_field = 'id'
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
#
#
# #APIView
#
#
# #--------dont ask for pk--------#
# #ListAPIView
# #CreateAPIView
#
#
# #----------asking for pk---------#
# #RetrieveAPIView
# #UpdateAPIView
# #DestroyAPIView
#
#
#
# #--------------------------------------------
# #I want to list and create both so that we can do by add both view like
# #ListAPIView + CreateAPIView = ListCreateAPIView
# from rest_framework.generics import ListCreateAPIView
# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# #------------------Retrieve and update both --------------#
# #RetrieveAPIView + UpdateAPIView = RetrieveUpdateAPIView
# from rest_framework.generics import RetrieveUpdateAPIView
# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# #--------------------Retrieve and destroy view----------
# from rest_framework.generics import RetrieveDestroyAPIView
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
#
# #--------------Retrieve & update  & Destroy--------- #
# #coz these 3 operation ask for pk
#
#
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
#
# #-----------all operation using 2 class only
# #ListCreate and RetrieveDestroyAPIView
#
#
# #http://localhost:8000/api-->list and create
# #http://localhost:8000/api/2/  --> delete update
