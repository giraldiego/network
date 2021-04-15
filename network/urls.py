
from django.urls import path

from . import views, api_views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("posts/", views.ProfilePostList.as_view(), name="post_list"),
    path("posts/<int:profile_pk>", views.ProfilePostList.as_view(),
         name="profile_post_list"),
    # path("profile/<int:pk>", views.ProfileDetailView.as_view(), name="profile_detail"),

    path("posts/create/", views.post_create, name="post_create"),

    path("api/posts/create/", api_views.post_create, name="api_post_create"),

]
