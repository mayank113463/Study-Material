from rest_framework import serializers
from testapp.models import Employee

#








#Session 14

#-------------ModelSerializer-----------------
#we dont need to specify explicilitly create update put and delete
#we dont need to define every field fo EmployeeSerializer explicilitly like model forms


def multiple_of_100(value):
    if value %100 != 0:
        raise serializers.ValidationError("employee salary should be multiple of 100")
class EmployeeSerializer(serializers.ModelSerializer):
    #if you want to perform validation for field level than you have to specify explicilitly that field
    #like esal
    esal = serializers.FloatField(validators=[multiple_of_100])
    class Meta:
        model = Employee
        fields = '__all__'
        #you can send specefic fields in tuples or list
        # fields = ['eno','eadd']
        #if you want only exclude some field than use
        #exclude = ['esal']















#Session 13
#
# from testapp.models import Employee
# #@inbuild validators example in FloatField
# def multiple_of_100(value):
#     if value %100 != 0:
#         raise serializers.ValidationError("employee salary should be multiple of 100")
# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=64)
#     esal = serializers.FloatField(validators=[multiple_of_100])
#     eadd = serializers.CharField(max_length=64)
#     #it will check at in serializer.is_valid in views.py for esal validation
#     #field level validation
#     def validate_esal(self,value):
#         if value < 1000:
#             raise serializers.ValidationError("employee salary should be greater than 50000")
#         return value
#     #objcet level validation for multiple fields
#     #here data  is python dict who took all field python
#     def validate(self,data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         if ename.lower() == 'sunny':
#             if esal<50000:
#                 raise serializers.ValidationError("sunny salary should be greater than 5000")
#         return data
#
#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)
#
#     #for put method also we have to oveeride update method
#     #and update existing ddata
#     #validated_data partner application provided data
#     #instance is current application existing object  in db
#     def update(self,instance,validated_data):   #update thease instance with validated_data
#         instance.eno = validated_data.get('eno',instance.eno)   #if there is change than change in data otherwise reman same
#         instance.ename = validated_data.get('ename',instance.ename)
#         instance.esal = validated_data.get('esal',instance.esal)
#         instance.eadd = validated_data.get('eadd',instance.eadd)
#         instance.save()
#         return instance
#
#
#
#
#
#
#
#


















#Session 10 -->12

#
# from testapp.models import Employee
# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=65)
#     esal = serializers.FloatField()
#     eadd = serializers.CharField(max_length=64)
#     #override create method and argument with validated_data which is for complex type data for db
#     def create(self,validated_data):
#         #here validated_data would have all records related to python dictionary objects
#         return Employee.objects.create(**validated_data)
#
#







#here serializers is like form and modelform from model
#on the behalf of models.IntegerField you have to write serializers.IntegerField()
#serialization: --> Employee object its python native datatype its not inbuild datatype
#converting complex types(queryset or model instance ) to python native data type(dict) called serialization

#1--> employee object to dictionary  --> json very easy
#for converting objcet to dictionary  in python shell-->
#from testapp.models import Employee
#from testapp.serializers import EmployeeSerializer
# emp = Employee.objects.get(id=1)  -->object instance
# eserializer = EmployeeSerializer(emp)    --> converting into python data type(dictionary)
# eserializer.data                          -->python dictionary
# from rest_framework.renderers import JSONRenderer  --> convert into json from python dictionary
# json_data = JSONRenderer().render(eserializer.data)   -->json form

# or
 #import json
# hi = json.dumps(eserializer.data)                     -->we can use it also to convert into json type
#Result  --->b'{"eno":3,"ename":"sunny","esal":5400.0,"eadd":"varansi"}'  here b for binary form



#How to perfomr serialization for queryset

#qs = Employee.objects.all()
# eserializer = EmployeeSerializer(qs,many =True)   # only many =True for qs
#eserializer.data---> result
#[OrderedDict([('eno', 1), ('ename', 'durga'), ('esal', 1234.0), ('eadd', 'allahabad')]), OrderedDict([('eno', 2), ('ename', 'mayank'), ('esal', 4000.0), ('eadd', 'banglore')]), OrderedDict([('eno', 3), ('ename', 'sunny'), ('esal', 5400.0), ('eadd', 'varansi')])]
# >>> json_data = JSONRenderer().render(eserializer.data)
# >>> json_data
# b'[{"eno":1,"ename":"durga","esal":1234.0,"eadd":"allahabad"},{"eno":2,"ename":"mayank","esal":4000.0,"eadd":"banglore"},{"eno":3,"ename":"sunny","esal":5400.0,"eadd":"varansi"}]'

#Serialization complex datatype to python native datatype






#Deserialization
#the process of converting python native data types into databases supported
#complex types is called Deserialization
# first partner application send data in json form convert it into python native datatype
#than convert into objcets type which supported to databases called Deserialization


#for json_data to python native datatype --> JSONParser
#import io
#from rest_framework import JSONParser
#stream  = io.BytesIO(json_data)  #json to string
#pdata = JSONParser().parse(stream)   #string to python native datatype

#by Deserialization we have to convert python data to db supported complex types
#serializer = EmployeeSerializer(data=pdata)
#now check is valid or not for db check
#serializer.is_valid()
#if serializer is valid
#serializer.validated_data   -->if valid than  it will convert into db support type using validated_data
#when converting into python to dict in serialization than we used serializer.data but here we have to use
#serializer.validated_data   -->db supported object form
#serializer.save()






#Use case of serialization and Deserialization
#1--> partner application wants all employee record in json format
#qs --> python native data type(serialization)
#python native datatype --> json data(JSONRenderer().render())  [Seeiralization]


#2.partner application sending json_data to create new employee
#json_data --> python native datatype(JSONParser().parse())
#python native data type -->db supported complex form [Deserialization]
