from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
MAG = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:MAG]
    title = "Последние обновления на сайте"
    context = {
        "title": title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:MAG]
    title = "Последние обновления на сайте"
    context = {
        "title": title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts//group_list.html', context)
