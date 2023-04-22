from django.db import models

# Create your models here.


class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS', 'HOT DEALS'),
        ('New Arraivels', 'New Arraivels'),
    )

    image = models.ImageField(upload_to='media/slider_imgs')
    discount_deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    sale = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name
    


class Banner(models.Model):
    image = models.ImageField(upload_to='media/slider_imgs')
    discount_deal = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    discount_text = models.CharField(max_length=200)
    link = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.quote
    

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.main_category.name + ' -- ' + self.name
    

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + ' -- ' + self.category.name + ' -- ' + self.name
    

class Section(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name