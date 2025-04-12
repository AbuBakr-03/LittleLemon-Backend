from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer
from rest_framework import status
from django.urls import reverse

class MenuItemTest(TestCase):
    def test_get_item(self):
        menu = Menu.objects.create(title='Lemon Icecream',price=4.00,inventory=4)
        self.assertEqual(str(menu),'Lemon Icecream : 4.0')
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Burger", price=9.99, inventory=5)
        self.item2 = Menu.objects.create(title="Salad", price=6.49, inventory=15)
        self.item3 = Menu.objects.create(title="Pizza", price=11.50, inventory=8)

    def test_getall(self):
        response = self.client.get(reverse('menu'))  # Make sure this name matches your URLconf
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)