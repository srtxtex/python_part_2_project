from django.test import TestCase
from django.urls import reverse
import sf_app.wsgi

class DjangoAppTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/home')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)