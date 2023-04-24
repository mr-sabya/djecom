from django.shortcuts import redirect, render
from app.models import Slider, Banner, Main_Category, Product

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