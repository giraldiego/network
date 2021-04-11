import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import User, Profile, Post


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def compose(request):
    # return HttpResponse("TODO compose")

    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check User credentials
    data = json.loads(request.body)
    user_pk = data.get("user_id")

    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return JsonResponse({
            "error": f"User does not exist."
        }, status=400)

    # Get contents of post
    content = data.get("content", "")

    # Create post with current timestamp
    timestamp = timezone.now()

    post = Post(
        content=content,
        author=user,
        timestamp=timestamp,
        likes=0
    )
    post.save()

    return JsonResponse({"message": "Post created successfully."}, status=201)


def posts_view(request):
    # return HttpResponse("TODO posts_view")
    # Filter emails returned based on mailbox
    # return JsonResponse({"error": "Invalid mailbox."}, status=400)

    # Return posts in reverse chronologial order
    posts = Post.objects.all().order_by("-timestamp")
    return JsonResponse([post.serialize() for post in posts], safe=False)


def profiles_view(request):
    return HttpResponse("TODO profiles_view")
