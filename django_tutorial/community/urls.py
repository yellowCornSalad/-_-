from django.urls import path
from .views import write, articleList, viewDetail


app_name = "community"
urlpatterns = [

    path('write/', write, name='write'),
    
    path('list/', articleList, name='list'),
    #/view_detail/1/
    
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
]