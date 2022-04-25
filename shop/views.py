from django.shortcuts import render

from shop.models import Category, Product

# Create your views here.

def products_list(request):
    categories = Category.objects.all()
    category = request.GET.get('category')
    products = Product.objects.all()
    products = products.filter(category=category) if category else products
    print(products[0].thumb.url)
    return render(request, 'product_list.html', {'products': products, 'categories': categories})