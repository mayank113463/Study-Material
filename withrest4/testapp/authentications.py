from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self,request):
        username = request.GET.get('username',)
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your credientials are invalid plz provide valid credentials')
        return (user,None)


#create custom authentication
#'key' lenght should be 7
#the first characters should be lower case alphabet symbol which should be last letter of username
#the third character should be 'Z'
#the 5th character should be first character of username
#http://127.0.0.1:8000/api/?username=villen&key=v7ZXn98 for postman
class CustomAuthentication2(BaseAuthentication):
    def authenticate(self,request):
        username = request.GET.get('username',)
        key = request.GET.get('key')
        if username is None or key is None:
            return None
        c1 = len(key) == 7 #if lenght is 7 than it will assign to the c1
        c2 = key[0]== username[-1].lower()
        c3 = key[2] == 'z'
        c4 = key[4] == username[0]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your credientials are invalid plz provide valid credentials')
        if c1 and c2 and c3 and c4:
            raise AuthenticationFailed('Your credientials are invalid plz provide valid credentials')
