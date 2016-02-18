import datetime

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.test.client import RequestFactory

from main.views import main, about


# Create your tests here.
class MainViewTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def test範本(self):
        request = self.factory.get(reverse('main:main'))
        with self.assertTemplateUsed('main/main.html'):
            response = main(request)
            self.assertEqual(response.status_code, 200)
    
    def test首頁時間(self):
        request = self.factory.get(reverse('main:main'))
        with self.assertTemplateUsed('main/main.html'):
            response = main(request) 
            self.assertIn(datetime.datetime.now().strftime('%Y年%m月%d日'), response.content.decode())


class AboutViewTest(TestCase):
    
    def setUp(self):   
        self.factory = RequestFactory()
        
    def test範本(self):
        request = self.factory.get(reverse('main:about'))
        with self.assertTemplateUsed('main/about.html'):
            response = about(request)
            self.assertEqual(response.status_code, 200)
    
    
   
        