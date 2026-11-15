from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductViewsTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test product',
            code='TEST-1',
            cost='10.00',
            discount=0,
            for_sale=True,
            category='Test',
            description='A product used for testing.',
            price='12.00',
        )

    def test_root_and_view_pages_render_products(self):
        for url in ('/', reverse('view')):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, self.product.name)
                if url == reverse('view'):
                    self.assertContains(response, self.product.code)

    def test_add_product(self):
        response = self.client.post(reverse('add'), {
            'name': 'New product',
            'code': 'NEW-1',
            'cost': '20.00',
            'discount': '5',
            'for_sale': 'on',
            'category': 'Test',
            'description': 'A newly added product.',
            'price': '25.00',
        })

        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Product.objects.filter(code='NEW-1').exists())

    def test_edit_product(self):
        response = self.client.post(reverse('edit_product', args=[self.product.id]), {
            'name': 'Updated product',
            'code': self.product.code,
            'cost': '10.00',
            'discount': '0',
            'for_sale': 'on',
            'category': 'Test',
            'description': 'An updated product.',
            'price': '15.00',
        })

        self.assertRedirects(response, reverse('home'))
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated product')
        self.assertEqual(str(self.product.price), '15.00')

    def test_delete_requires_post(self):
        url = reverse('delete_product', args=[self.product.id])

        self.assertEqual(self.client.get(url).status_code, 405)
        response = self.client.post(url)

        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_missing_product_returns_404(self):
        response = self.client.get(reverse('product_details', args=[9999]))

        self.assertEqual(response.status_code, 404)
