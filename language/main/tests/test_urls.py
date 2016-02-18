from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from main.views import main, about


# Create your tests here.
class MainURLTest(TestCase):

    
    def test首頁路徑(self):
        found = resolve('/')
        self.assertEqual(found.func, main)
        
    def test關於路徑(self):
        found = resolve(reverse('main:about'))
        self.assertEqual(found.func, about)