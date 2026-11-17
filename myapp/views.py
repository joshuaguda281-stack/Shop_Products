from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Product
from .my_forms import ProductForm, SignUpForm


@login_required
def home(request):
    products = Product.objects.all()
    # for product in products:
    #      print(f"Product Name: {product.name}, Code: {product.code}, Price: {product.price}")
    return render(request, 'home.html',  {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product {form.name} permanently added')
            return redirect('home')
    else:
        form = ProductForm()
    messages.success(request, 'Product added successfully')
    return render(request, 'add.html', {'form': form})

@login_required
def view_products(request):
    products = Product.objects.all()
    messages.success(request, 'Products displayed successfully')
    return render(request, 'view.html', {'products': products})


@require_POST
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, f'Product {product.name} permanently deleted')
    return redirect('home')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product {product.name} successfully updated')
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form, 'product': product})

@login_required
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'details.html', {'product': product})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('home')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
