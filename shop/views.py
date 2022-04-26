from django.shortcuts import render
from shop.models import Brand, Category, Product, Slide
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/sign_in')
def products_list(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    products = Product.objects.all()
    slides = Slide.objects.all()
    products = products.filter(category=category) if category else products
    products = products.filter(brand = brand) if brand else products
    return render(request, 'product_list.html', {'products': products, 'categories': categories, 'brands': brands, 'slides': slides})














