
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_django,name = 'django'),
    path('<int:chai_id>/',views.chai_detail,name= 'chai_description')
]
