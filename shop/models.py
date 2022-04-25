from distutils.command import upload
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('Category', default=None,   on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', default=None, on_delete=models.CASCADE)
    thumb = models.ImageField(default='no_product.png', upload_to="images/", null=True)

    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'


class Brand(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_brands'


class User(models.Model):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100, null=True)