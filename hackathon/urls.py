from django.urls import path
from . import views

app_name = 'hackathon'
urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path("register_for_hackthon/show_submissions/<int:hackathon_id>", views.show_submissions,name="submissions"),
    path('register_for_hackthon/show_submissions/make_submission/<int:hackathon_id>',views.make_submissions, name='submission'),
    path("hackathon", views.add_hackthon, name="add_hackathon"),
    path("register_for_hackthon/<int:id>",views.register_for_hackathon, name="register"),
]
