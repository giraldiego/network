
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("posts/", views.PostList.as_view(), name="post_list"),
    path("profile/<int:pk>", views.ProfileDetailView.as_view(),
         name="profile_detail"),

]
