from django.conf.urls import url
from vitApp import views
from django.urls import path

app_name = 'vitApp'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name='VDD'),
]
