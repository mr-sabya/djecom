from django.shortcuts import redirect, render
from app.models import Slider

def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = Slider.objects.all()

    context = {
        'sliders': sliders,
    }
    return render(request, 'home/index.html', context)