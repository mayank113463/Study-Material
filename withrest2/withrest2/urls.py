#sessions 15


# from django.contrib import admin
# from django.urls import path
# from testapp import views
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', views.TestAPIView.as_view()),
#
# ]


#------------------ViewSet url and routers-------------->


from django.contrib import admin
from django.urls import path,include
from testapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# register our view to DefaultRouter
router.register('test-view-set',views.TestViewSet,base_name='test-view-set')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('api/', views.TestAPIView.as_view()),

]
