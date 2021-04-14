
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<int:profile_pk>", views.ProfilePostList.as_view(), name="profile_post_list"),
    path("profile/<int:pk>", views.ProfileDetailView.as_view(),
         name="profile_detail"),


]
