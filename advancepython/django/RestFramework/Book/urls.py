
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
path('GetAllBooks/',views.getBooks),
path('addbook/',views.addBook),
path('getbyid/<int:pk>',views.getById),
#    path('deletebyid/<int:id>',views.deleteById),
#    path('updatebyid/<int:id>',views.updateById)
]
