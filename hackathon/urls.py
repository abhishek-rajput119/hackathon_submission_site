from django.urls import path
from . import views

app_name = 'hackathon'
urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('add',views.add_hackthon, name='submission'),
    path("hackathon/<int:id>", views.add_hackthon, name="add_hackathon")
]
