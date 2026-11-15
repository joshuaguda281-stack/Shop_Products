import uuid

from django.db import models

def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return f'products/{new_filename}'
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=gen_unique_path, default='products/default.jpg')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
       db_table = 'products'

# Run Migrations
# Python manage.py makemigrations
#python manage.py migrate