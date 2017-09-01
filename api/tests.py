from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Visitor

class ModelTestCase(TestCase):
    """This class defines the test suite for the visitor model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.visitor_rfid = "9464d70e"
        self.visitor_fullname = "Michel Vuijlsteke"
        self.visitor = Visitor(rfid=self.visitor_rfid, fullname=self.visitor_fullname)

    def test_model_can_create_a_visitor(self):
        """Test the visitor model can create a visitor"""
        old_count = Visitor.objects.count()
        self.visitor.save()
        new_count = Visitor.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for api views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.visitor_data = {'rfid': '9464d70e', 'fullname': 'Michel Vuijlsteke'}
        self.response = self.client.post(
            reverse('create'),
            self.visitor_data,
            format="json")

    def test_api_can_create_a_visitor(self):
        """Test the api can create a visitor"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_visitor(self):
        """Test the api can get a given visitor."""
        visitor = Visitor.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': visitor.rfid}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, visitor)

    def test_api_can_update_visitor(self):
        """Test the api can update a given visitor."""
        change_visitor = {'fullname': 'Blah'}
        res = self.client.put(
            reverse('details', kwargs={'pk': visitor.rfid}),
            change_visitor, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_visitor(self):
        """Test the api can delete a visitor."""
        visitor = Visitor.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': visitor.rfid}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)