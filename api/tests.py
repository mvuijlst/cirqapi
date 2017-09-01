from django.test import TestCase
from .models import Visitor

class ModelTestCase(TestCase):
    """This class defines the test suite for the visitor model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.visitor_rfid = "9464d70e"
        self.visitor = Visitor(rfid=self.visitor_rfid)
    
    def test_model_can_create_a_visitor(self):
        """Test the visitor model can create a visitor"""
        old_count = Visitor.objects.count()
        self.visitor.save()
        new_count = Visitor.objects.count()
        self.assertNotEqual(old_count, new_count)