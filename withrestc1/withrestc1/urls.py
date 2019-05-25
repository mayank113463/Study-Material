
from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/',views.EmployeeCRUDCBV.as_view())
]
