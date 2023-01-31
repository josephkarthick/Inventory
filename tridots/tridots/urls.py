
from django.contrib import admin
from django.urls import path
from invent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.viewpro,  name='viewproduct'),
    path ('addproduct/',  views.addpro,   name='addproduct'),
    path ('editpro/<int:pdid>', views.editpro,  name='editpro'),
    
    path ('viewlocation/', views.viewloc,  name='viewlocation'),
    path ('addlocation/',  views.addloc,   name='addlocation'),
    path ('viewlocation/editlocation/<int:ltid>', views.editloc,  name='editlocation'),
    
    
    path ('viewmovement/', views.viewmvmnt, name='viewmovement'),
    path ('addmovement/',  views.addmvmnt, name='addmovement'),
    path ('editmovement/', views.editmvmnt, name='editmovement'),
]
