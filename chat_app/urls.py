from django.urls import path
from . import views

urlpatterns =[
    path('livechat/',views.main_view,name='chat'),

]