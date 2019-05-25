#session 23



from django.contrib import admin
from django.urls import path,include
from testapp import views
from rest_framework import routers

# from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV,base_name='api')

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('get-api-token/',views.obtain_auth_token,name='get-api-token'),
    #--------------jwt token based -->
    path('auth-jwt/',obtain_jwt_token),
    path('auth-jwt-refresh/',refresh_jwt_token),
    path('auth-jwt-verify/',verify_jwt_token),
]














#session 20

#
# from django.contrib import admin
# from django.urls import path,include
# from testapp import views
# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# router.register('api',views.EmployeeCRUDCBV,base_name='api')
#
#
# #from authtoken class multiple views  to get token
# #FBV -->obtaine_auth_token present inside views
# #if user demands for token
# #http POST http://127.0.0.1:8000/get-api-token/ username="user" password="1234"
#
# from rest_framework.authtoken import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include(router.urls)),
#     path('get-api-token/',views.obtain_auth_token,name='get-api-token'),
#
# ]


#session 19

#
# from django.contrib import admin
# from django.urls import path,include
# from testapp import views
# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# router.register('api',views.EmployeeCRUDCBV,base_name='api')
# #here for model base viewset so base_name is optoional
#
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include(router.urls)),
#
# ]
