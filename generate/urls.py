from django.urls import path
from .import views

urlpatterns = [
    path("index/" , views.index, name="index"),
    path("random/" , views.random_avatar, name="random"),
    path("" , views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("generate/<str:seed>", views.avatar_input, name="avatar")
]
