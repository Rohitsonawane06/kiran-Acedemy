
from django.urls import path,include

from .import views
urlpatterns= [
    path('',views.show,name="show"),
    path('add/',views.add,name="add"),
    path('update/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('search/', views.search_view, name='search'),
    path('login/',views.login,name='login'),
    path('register/',views.logoutU,name='logout'),
    path('logout/',views.login,name='login'),

]
