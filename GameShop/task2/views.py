from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-created_at')  # все посты сортируем по дате
    page_size = request.GET.get('page_size', 3)
    paginator = Paginator(posts, page_size)  # три поста на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj})



