#i want to create a custom permission class which allow only safe methods like
# get option head


from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        print("hi")
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGETOrPatch(BasePermission):
    def has_permission(self,request,view):
        print("hello")
        allowed_methods= ['GET','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False

#if name is sunny than perform all method allowed
#if name is not sunny and name contains even number of characters thn all safe methods allowed
#otherwise no permission

class SunnyPermission(BasePermission):
    def has_permission(self,request,view):
        username = request.user.username
        print("hellohello")
        if username.lower() == 'sunny':
            return True
        elif username !='' and len(username) %2 == 0 and request.method in SAFE_METHODS:
            return False
        else:
            return False
        allowed_methods= ['GET','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False
