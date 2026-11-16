from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Product
from .my_forms import ProductForm

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


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Perform login logic here
            # Perform login logic here
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')


    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    return None

@login_required
def logout(request):
    if request.method == 'POST':
        logout(request)  # Perform logout logic here
        messages.success(request, 'Logout successful')
    return redirect('login')