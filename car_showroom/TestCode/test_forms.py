from django.test import SimpleTestCase
from showroom.forms import CustomerForm
import fileinput

class TestForms(SimpleTestCase):
    
    def test_customer_form_no_data(self):
        form = CustomerForm(data={})
        self.assertFalse(form.is_valid())


    def test_customer_form_with_data(self):
        x = fileinput.input(files ='C:\\Users\\Administrator\\Documents\\GitHub\\CSE470-project\\Untitled.png')
       
        form = CustomerForm(data={
            'file' : x
        })
        self.assertFalse(form.is_valid())