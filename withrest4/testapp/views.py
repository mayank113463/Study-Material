from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer

#Session 21
#1-->AllowAny--> for that disable for any view class
#2-->IsAuthenticated --> only authenticated can access end point or only register users
#3-->IsAdminUser --> only admin can access means staff status true

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAdminUser
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [IsAdminUser,]



#4-->IsAuthenticatedOrReadOnly -->for read only operation
#like Get,Head ,and options -->than no need to authenticated
#But for Write operation -->POST,PUT,PATCH,DELETE
#IRCTC -->Trains information to book the tcikets but for book he has to login
#BookMyShow

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [IsAuthenticatedOrReadOnly,]
#




#5--> DjangoModelPermissions:
#here we have complete control all permission
#if you want to access end point -->Authentication Required
#GET--> authentication is enough models permissions not Required
#POST,PUT,PATCH,DELETE -->authentication + model permission Required

#here a model permission-->
#POST--> add model permission
#PUT ,PATCH--> change model permission
#DELETE--> delete model permission

#for giving model permission go to user through superuser login
#User Permission is there find the app name and that model change that can change and delete/......

#
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import DjangoModelPermissions
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [DjangoModelPermissions,]
#


#6--> DjangoModelPermissionsOrAnonReadOnly:
#read operation can do anyone anomynoumous person no token no authentication not Required
#but for post delete Required both model + authentication
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]
#


#Session 22
#7-->Custom permmission class
#permission class should be child class of BasePermission
#and we have to override has_permission class
#in permissions.py in testapp
# class XYZPermission(BasePermission):
#     has_permission(self,request,view)

# from testapp.permissions import IsReadOnly,IsGETOrPatch,SunnyPermission
# from rest_framework.authentication import TokenAuthentication
# # from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
#
#
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [SunnyPermission,]



#for TokenAuthentication perfomance will be down DRF inbuild authentication
#To overcome this problem we should go for JWT json web token authorization
#jWT provide user details alos

#------------JWT(Json Web TOken)Authentication---------------#
#id don not need to communicate with databases.
#perfomance wise best
#its not from DRF .other package are there
#1-djangorestframework-jWT
#2->django-rest_framework-simplejwt
#install->pip install djangorestframework-jwt

#--------steps--
#1-access token  --> 5 min expiration time provide security
#2-refresh token  --> renew like passport new token non expired tokens can be refreshed to obtain a brand new token with renew expiration time
#refresh token should be done before access token exxpirations
#in settings.py do
#only for 7 days refresh token

#3-verify token-->if token is valid than it will provide 200 status same token returned
#otherwise 400 status code
#jwt.views generate token

#to generate aceess token:username and pwd and +db connection Required
#urls.py -->for getting token ,for refrshing token ,for verify token


#get token from cmd-->http http://127.0.0.1:8000/auth-jwt/ username="villen" password="mayank007"
#postman -->post method   http://127.0.0.1:8000/auth-jwt/ in body write username and password


#check verify token--> http POST http://127.0.0.1:8000/auth-jwt-verify/token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InZpbGxlbiIsImV4cCI6MTU1ODU5MDAxMSwiZW1haWwiOiIifQ.KhKv2VjPg2QFe5LRmAVJiK6JlhcFpoowS4RuQkongT4"
#postman in body write token and value and give post ethod to check its expired or not


#refresh token-->
#in settings.py JWT_ALLOW_REFRESH = True
#contenttypes-->application/json in posman
#in this token three dots is present like xxx.yyy.zzz header.payload.signature first is header 2nd is payload 3rd is signature
#so after refreshing only signature or 3rd part changing


#--------------How to enable json token for views.py----------#


#
#Session 24
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [JSONWebTokenAuthentication,]
#     permission_classes = [IsAuthenticated,]


#for JWT
# JWT_AUTH={
#     'JWT_ALLOW_REFRESH':True,
#     'JWT_AUT_HEADER_PREFIX':'JWT'   here prefex can be anyname fro authorization token
# }
#

# http://127.0.0.1:8000/api/ now give in headers get and in Authorization -->JWT <tokne>
#it will give the result




#---------------cutomize time for Time for Token-----------
## JWT_AUTH={
#     'JWT_ALLOW_REFRESH':True,
#     'JWT_AUT_HEADER_PREFIX':'JWT'   here prefex can be anyname fro authorization token
#       'JWT_EXPIRATION_DELTA': datetime:timedelta(seconds=300)
#}
#





#Sessinon 25


#-----------Custom Authentication-------------# very rare uses
#custom authentication class extends BaseAuthentication
#autheticate() method for oveeride
#Return tuple: (user,None)
#AuthenticationFailed exception for failed


#in authentication.py class create CustomAuthentication
#postman     -----http://127.0.0.1:8000/api/?username=villen------
##http://127.0.0.1:8000/api/?username=villen&key=v7ZXn98 for postman CustomAuthentication2
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from testapp.authentications import CustomAuthentication2
#
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [CustomAuthentication2,]
#     permission_classes = [IsAuthenticated,]
#     # authentication_classes = [JSONWebTokenAuthentication,]
#     # permission_classes = [IsAuthenticated,]
#





#-------------------Session 26---------------#
#Pagination :
#3 Pagination classes are theere
#I-PageNumberPagination
#II-LimitOffsetPagination
#III-CursorPagination

#Enable pagination globally:
#in settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 100
# }


#Enable Pagination locally :
##### Class EmployeeAPIView(generics.LISTAPIView
######     pagination_class =10















































#Session 19 & 20
#-----------------Authentication types 4 types
#basic Authentication ,session Authentication ,token Authentication ,josn Authentication

#-------------Authorization------------
#multiple permission classes
#--1->AllowAny,  2-->IsAuthenticated ,3-->IsAdminUser
#  4-->IsAuthenticatedOrReadOnly, 5-->DjangoModelPermissions
#    6-->DjangoModelPermissionsOrAnonReadOnly



#after Authentication provide Authorization



#READ operation  : GET,OPTIONS,HEAD   ==>Safe methods
#Write operation : POST ,PUT,PATCH,DELETE  ==>Unsafe methods


#----------Token Authentication-------------#
#Authentication perform by some token
#best choice for desktop clients ,mobile clients


#token must be Generated #token must be validated by
#authtoken -->[DRF provided ]

#include authtoken in settings.py
#when token will generate than it will store in any table thats called
#Tokens table  -->part of authtoken
#migrate
#you have to create tokens for  users
#to get Authentication token so you have to send using --> urls.py
#it will give respective token
#http POST http://127.0.0.1:8000/get-api-token/ username="user" password="1234"
#
#-----------authtoken------------
#1->authtoken application can validate this username and password
#2--> authtoken application will check whether token already Generated for this user or # NOT
#3--> if token already generated for this user than existing token will be return
#4--> if token not generated

#--------------Authorization----------#
#now we have to specify Authorization in views
#enable Authorization for users
#locally its example

#
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     #for Authorization token Authorization is a class so we have to import that
#     #and add in authentication_classes
#     authentication_classes = [TokenAuthentication,]
#     #provide is autheticated or not
#     permission_classes = [IsAuthenticated,]
#     # access using this in cmd
#     # http http://127.0.0.1:8000/api/ "authorization:Token  ae68a54f9cdfe3b58d75e87dbb8f0bdbeffd0d91"
#     #in postman for authorization check in headers put input


#for every class we have to write that TokenAuthentication
#so enable authentication globally in settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION-CLASSES':('rest_framework.authentication.TokenAuthentication',),
#     'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',)
# }

#globally secure
# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]




#if you dont want locally one class dont ask for permmisson than define class level
#and its overrid globally security classess













#session 19

# class EmployeeCRUDCBV(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
