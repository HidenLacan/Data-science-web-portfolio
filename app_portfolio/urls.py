
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='index'),
    path('about/',views.About.as_view(),name='about'),
    path('projects/',views.Projects.as_view(),name='projects'),
    path('resume/',views.Resume.as_view(),name='resume'),
]
