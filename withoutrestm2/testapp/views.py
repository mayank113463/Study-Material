from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import HttpResponseMixin
import json
from testapp.models import Student
from testapp.mixins import SerializeMixin

from testapp.forms import StudentForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#Session 10
#rest api again without rest framework for this webapp
#mixin is a class use for code reusablity purpose

@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    #for getting id he can pass id or not pass id
    #if pass give the id related data otherwise give all response
    def get_object_by_id(self,id):
        try:
            s = Student.objects.get(id=id)
        except:
            s = None
        return s

    def get(self ,request, *args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None)

        if id is not None:
            # std = Student.objects.get(id=id)
            std = self.get_object_by_id(id)
            #if record is not available
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'No maching record found'}),status=400)
            json_data = self.serialize([std,])
            return self.render_to_http_response(json_data)

        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)



    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
        std_data = json.loads(data)

        #to save in db form must be requied

        form = StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'resource insert successfully'}),status=200)
        if form.errors:
            json_data= json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json'}),status=400)
        provided_data = json.loads(data)
        id = provided_data.get('id',None)

        if id is None:
            return self.render_to_http_response(json.dumps({'msg':' to perform updation id is medatory '}),status=200)
        std = self.get_object_by_id(id)

        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'fields for matched found'}),status=400)
        original_data = {
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'resource updated successfully'}),status=200)
        if form.errors:
            json_data= json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

        # return self.render_to_http_response(original_data)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json'}),status=400)
        provided_data = json.loads(data)
        id = provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':' id is medatory to delete '}),status=200)
        std = self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'not possible to delete '}),status=400)

        status, deleted_item = std.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'resource deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg': 'unable to delete please try again'})
        return self.render_to_http_response(json_data)
