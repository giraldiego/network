import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.utils import timezone

from .models import User, Profile, Post


@login_required
def post_create(request):

    # Creating a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check not empty content
    data = json.loads(request.body)
    content = data.get("content")
    if not content:
        return JsonResponse({
            "error": "Posts with empty content are not allowed."
        }, status=400)

    #  Set values
    author = request.user
    timestamp = timezone.now()
    likes = 0

    post = Post(
        content=content,
        author=author,
        timestamp=timestamp,
        likes=likes,
    )
    post.save()

    return JsonResponse({"message": "Post saved successfully."}, status=201)
