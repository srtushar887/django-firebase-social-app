from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('firebase/users',views.filrebaseusers,name="filrebaseusers"),
    path('firebase/users/delete/<str:uid>',views.userdelete,name="userdelete"),
    path('firebase/users/posts/<str:uid>',views.filrebaseusersposts,name="filrebaseusersposts"),
]