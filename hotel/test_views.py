from django.test import TestCase, Client
from .models import Booking
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestBookingViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='viewstest',
            email='viewstest@test.com',
            password='viewtest')
        self.client.login(
            username='viewstest',
            email='viewstest@test.com',
            password='viewtest'
            )

        self.booking_url = reverse('book')
        self.mybookings_url = reverse('mybookings')

        self.booking1 = Booking.objects.create(
            user_id=1,
            full_name='Test Booking',
            email='viewstest@test.com',
            phone_number='+447311490765',
            num_adults=1,
            num_children=1,
            check_in='2022-10-30',
            check_out='2022-10-31',
            room=1,
        )

        self.edit_booking1_url = reverse('edit', args=[1])
        self.delete_booking1_url = reverse('delete', args=[1])

    def test_make_booking_GET(self):
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

    def test_get_my_bookings(self):
        response = self.client.get(self.mybookings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_bookings.html')

    def test_edit_booking_GET(self):
        response = self.client.get(self.edit_booking1_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')

    def test_delete_booking_GET(self):
        response = self.client.get(self.delete_booking1_url)
        self.assertRedirects(response, '/mybookings')
        existing_items = Booking.objects.filter(id=1)
        self.assertEqual(len(existing_items), 0)

    def test_redirects_if_not_logged_in_when_booking(self):
        self.client.logout()
        response = self.client.get(self.booking_url)
        self.assertRedirects(response, '/accounts/login/?index=/booking')
