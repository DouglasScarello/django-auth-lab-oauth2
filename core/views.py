from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.order_by("-id")[:20]
    context = {
        "mensagem": "Douglas dominando Django",
        "posts": posts
    }
    return render(request, "core/home.html", context)



from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required
def criar_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, "Post criado com sucesso! 🚀")
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "core/criar_post.html", {"form": form})