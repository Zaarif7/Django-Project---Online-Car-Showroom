from django.test import SimpleTestCase
from django.urls import reverse, resolve
from showroom.views import signup, login, search, logout, index, car_products, about_us, accessories, singleaccessory, singlecar, contact_us, booking, createbooking, profile, updateprofile

class TestUrls(SimpleTestCase):

    '''Total 9 public functions are tested here'''

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, signup)
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, login)
    
    def test_search_url_is_resolved(self):
        url = reverse('search')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, search)
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, logout)

    def test_car_products_url_is_resolved(self):
        url = reverse('car-products')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, car_products)

    def test_about_us_url_is_resolved(self):
        url = reverse('about-us')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, about_us)

    def test_accessories_url_is_resolved(self):
        url = reverse('accessories')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, accessories)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        #print(resolve(url)) 
        self.assertEquals(resolve(url).func, profile)

    def test_updateprofile_url_is_resolved(self):
        url = reverse('updateprofile')
        #print(resolve(url)) 
        self.assertEquals(resolve(url).func, updateprofile)

    








































































































































































































































































