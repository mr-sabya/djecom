from django.shortcuts import redirect, render
from app.models import Slider, Banner, Main_Category

def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    banners = Banner.objects.all().order_by('-id')[0:3]
    main_categories = Main_Category.objects.all().order_by('name')

    context = {
        'sliders': sliders,
        'banners': banners,
        'main_categories': main_categories
    }
    return render(request, 'home/index.html', context)