from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = "Последние обновления на сайте"
    context = {
        "title": title,
        "text": "Это главная страница проекта yatube",
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = "Последние обновления на сайте"
    context = {
        "title": title,
        "text": "Здесь будет информация о группах yatube",
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts//group_list.html', context)
