# Create your views here.
from django.shortcuts import render, redirect
from myapp.models import Product
from .my_forms import  ProductForm

def home(request):
    products = Product.objects.all()
    # for product in products:
    #      print(f"Product Name: {product.name}, Code: {product.code}, Price: {product.price}")
    return render(request, 'home.html',  {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = ProductForm()

    # Product.objects.get_or_create(
    #     code="P001",
    #     defaults=dict(name="Unga", cost=150.00, discount=0, for_sale=True,
    #                   category="foods", description="Energy giving", price=170.00),
    # )
    # Product.objects.get_or_create(
    #     code="P101",
    #     defaults=dict(name="Chapati", cost=20.00, discount=0, for_sale=True,
    #                   category="foods", description="Energy giving", price=50.00),
    # )
    # Product.objects.get_or_create(
    #     code="P008",
    #     defaults=dict(name="Laptop", cost=30_000.00, discount=0, for_sale=True,
    #                   category="electronics", description="High performance",
    #                   price=35_000.00),
    #
    return render(request, 'add.html', {'form': form})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view.html', {'products': products})