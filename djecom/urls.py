from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [

    #errors
    path('404', views.Error404, name='404'),

    path('admin', admin.site.urls),
    path('base', views.BASE, name='base'),

    path('', views.HOME, name='index'),
    path('product/<slug:slug>', views.PRODUCT_DETAILS, name='product_details'),


    # account paths
    path('account/my-account', views.MY_ACCOUNT, name='my_account'),
    path('account/register', views.REGISTER, name='register'),
    path('account/login', views.LOGIN, name='login'),

] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
