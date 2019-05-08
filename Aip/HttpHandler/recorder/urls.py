from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upaload, name="upload"),
    path('result/<id>', views.result, name="result"),
    path('test/', views.test, name="test"),
    path('table/', views.table_list, name="table"),
    path('download/', views.download, name="download"),
    #path('remove/', views.download, name="remove"),
]

