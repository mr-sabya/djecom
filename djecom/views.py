from django.shortcuts import redirect, render
from app.models import Slider, Banner, Main_Category, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    banners = Banner.objects.all().order_by('-id')[0:3]
    main_categories = Main_Category.objects.all().order_by('name')
    deal_products = Product.objects.filter(section__name = "Top Deals Of The Day")

    context = {
        'sliders': sliders,
        'banners': banners,
        'main_categories': main_categories,
        'deal_products': deal_products
    }
    return render(request, 'home/index.html', context)



def PRODUCT_DETAILS(request, slug):
    product = Product.objects.filter(slug = slug)

    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'product': product,
    }
    return render(request, 'product/show.html', context)


def Error404(request):
    return render(request, 'errors/404.html')


def MY_ACCOUNT(request):
    return render(request, 'account/my-account.html')


def REGISTER(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()

    return redirect('my_account')



def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Email and Password Are Invalid!')
            return redirect('my_account')
    return render(request, 'account/my-account.html')