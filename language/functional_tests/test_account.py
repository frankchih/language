import datetime

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver 


class VisitorTest(LiveServerTestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.startup.homepage', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url.additional',      'about:blank')
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(2)

    
    def tearDown(self):
        self.browser.quit()


    def test使用者操作首頁(self):
        '''
        測試使用者在首頁的各項操作
        '''

        #使用者聽說有一個很酷的程式語言小百科，她前往它的首頁
        self.browser.get(self.live_server_url) 
    
        #她注意到首頁的標題提到了程式語言小百科
        self.assertEqual('程式語言小百科', self.browser.title)
        
        #網站會顯示現在的時間
        body = self.browser.find_element_by_tag_name('body')
        
        self.assertIn(datetime.datetime.now().strftime('%Y年%m月%d日'), body.text)
        
        #看到關於，程式百科，註冊，登入的連結
        links = self.browser.find_elements_by_tag_name('a')
        self.assertTrue(any(link.text=='關於' for link in links))
        self.assertTrue(any(link.text=='程式百科' for link in links))
        self.assertTrue(any(link.text=='註冊' for link in links))
        self.assertTrue(any(link.text=='登入' for link in links))        
        
        #點擊關於，出現的「關於」頁面
        self.browser.get(self.live_server_url+reverse('main:about'))
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('關於', body.text)
        
        #出現回首頁連結
        link = self.browser.find_element_by_tag_name('a')
        self.assertIn('回首頁', link.text)
        self.fail('測試未完成')
        
        
        
        




