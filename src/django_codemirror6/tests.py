from django.test import Client
from django.test import TestCase as DjangoTestCase
from django.urls import reverse


class TestCase(DjangoTestCase):
    def test_demo(self):
        client = Client()
        response = client.get(reverse('demo'))
        assert response.status_code == 200
