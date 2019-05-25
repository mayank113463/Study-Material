#session 18


from django.contrib import admin
from django.urls import path,re_path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/$', views.EmployeeListCreateModelMixins.as_view()),
    re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeRetrieveUpdateDestroyModelMixins.as_view()),


]















#Session 16 & 17


# from django.contrib import admin
# from django.urls import path,re_path
# from testapp import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('api/', views.EmployeeListAPIView.as_view()),
#     # path('api/', views.EmployeeCreateAPIView.as_view()),
#     # re_path(r'^api/(?P<id>\d+)/$', views.EmployeeRetrieveAPIView.as_view()),
#     # re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeUpdateAPIView.as_view()),
#     # re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeDestroyAPIView.as_view()),
#     # path('api/', views.EmployeeListCreateAPIView.as_view()),
#     # re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeRetrieveUpdateAPIView.as_view()),
#     # re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeRetrieveDestroyAPIView.as_view()),
#     re_path(r'^api/(?P<pk>\d+)/$', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
#     re_path(r'^api/$', views.EmployeeListCreateAPIView.as_view()),
#
#
# ]
