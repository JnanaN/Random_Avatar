from django.urls import path
from .import views

urlpatterns = [
    path("" , views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("index/" , views.index, name="index"),
    path("generate/<str:seed>", views.avatar_input, name="avatar"),
    path("random/" , views.random_avatar, name="random"),    
]
