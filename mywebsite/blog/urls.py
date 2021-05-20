from django.urls import path
from blog import views
from django.views.generic import TemplateView


#app_name = 'web'
urlpatterns = [
    path("", views.index, name="index"),
    #path("", views.result, name="result")
    path("selectTitle/", views.selectTitle, name="selectTitle"),
    path("selectTag/", views.selectTag, name="selectTag"),
]

