from django.test import TestCase
from showroom.models import Customer, Products, Booking, Manufacturer, Car, Accesories, UserMessage


class TestModels(TestCase):
    
    def test_Customer(self):
        customer1 = Customer.objects.create(name='customer1')
        self.assertEquals(self.customer1.name, 'customer1')

    def test_Products(self):
        Products1 = Products.objects.create(name='Products1')
        self.assertEquals(self.Products1.name, 'Products1')  

    def test_Booking(self):
        Booking1 = Booking.objects.create(name='Booking1')
        self.assertEquals(self.Booking1.name, 'Booking1')  

    def test_Manufacturer(self):
        Manufacturer1 = Manufacturer.objects.create(name='Manufacturer1')
        self.assertEquals(self.Manufacturer1.name, 'Manufacturer1') 

    def test_Car(self):
        Car1 = Car.objects.create(name='Car1')
        self.assertEquals(self.Car1.name, 'Car1')
        
    def test_Accesories(self):
        Accesories1 = Accesories.objects.create(name='Accesories1')
        self.assertEquals(self.Car1.name, 'Accesories1')    

    def test_UserMessage(self):
        UserMessage1 = UserMessage.objects.create(name='UserMessage1')
        self.assertEquals(self.Car1.name, 'UserMessage1') 