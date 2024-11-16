from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserReg
from .models import Buyer, Game

# Create your views here.


def sign_up_by_django(request):
    info = {}
    #users = Buyer.objects.values_list('name', flat=True)
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = Buyer.objects.values_list('name', flat=True)
            if password != repeat_password:
                info["error"] = 'Пароли не совпадают'
                return HttpResponse(f'Error,{info["error"]}!')
            elif int(age) < 18:
                info["error"] = 'Вы должны быть старше 18'
                return HttpResponse(f'Error,{info["error"]}!')
            elif username in users:
                info["error"] = 'Пользователь уже существует'
                return HttpResponse(f'Error,{info["error"]}!')
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'
                return HttpResponse(f"Приветствуем,{username}")
    else:
        form = UserReg()
    return render(request, 'main/registration_page.html', context={'info': info})


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        user_all = Buyer.oblects.all()
        users = [user.name for user in user_all]
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f'Error,{info["error"]}!')
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(f'Error,{info["error"]}!')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse(f'Error,{info["error"]}!')

        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            info['message'] = f'Приветствуем, {username}!'
            return HttpResponse(f"Приветствуем,{username}")
    return render(request, 'main/registration_page.html', context=info)


def platform(request):
    return render(request, 'main/platform.html')


def games(request):
    game = Game.objects.all()
    contex = {
        'games': game
    }
    return render(request, 'main/games.html', contex)


def cart(request):
    return render(request, 'main/cart.html')

