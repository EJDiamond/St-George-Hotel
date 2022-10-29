from django.test import TestCase
from .forms import BookingForm, ContactForm


class TestBookingForm(TestCase):
    """ Test the booking form """
    def test_all_fields_are_required(self):
        """ Check all fields are required by creating an empty form and
            checking that it is not valid.
            Check field key names are in the form errors dict.
            Check the error returned for empty fields is correct """
        form = BookingForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'num_adults': '',
            'num_children': '',
            'check_in': '',
            'check_out': '',
            'room': '',
        })
        self.assertFalse(form.is_valid())

        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('num_adults', form.errors.keys())
        self.assertIn('num_children', form.errors.keys())
        self.assertIn('check_in', form.errors.keys())
        self.assertIn('check_out', form.errors.keys())
        self.assertIn('room', form.errors.keys())

        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')
        self.assertEqual(
            form.errors['num_adults'][0], 'This field is required.')
        self.assertEqual(
            form.errors['num_children'][0], 'This field is required.')
        self.assertEqual(
            form.errors['check_in'][0], 'This field is required.')
        self.assertEqual(
            form.errors['check_out'][0], 'This field is required.')
        self.assertEqual(
            form.errors['room'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Check the Meta fields are equal to that defined in the Meta class """
        form = BookingForm()
        self.assertTrue(form.Meta.fields, [
            'full_name',
            'email',
            'num_adults',
            'num_children',
            'room',
            ]
        )

    def test_date_fields_have_widgets(self):
        """Test check in and check out fields have DateInput widget attached"""
        form = BookingForm()
        self.assertEqual(
            form.fields['check_in'].widget.__class__.__name__, 'DateInput')
        self.assertEqual(
            form.fields['check_out'].widget.__class__.__name__, 'DateInput')

    def test_phone_number_is_correct_format(self):
        """ Test that the phone number field, must be +44 format """
        form = BookingForm({
            'phone_number': '07311490876'
        }
        )
        self.assertFalse(form.is_valid())

    def test_adults_default_is_one(self):
        """Check number of adults field is initially set to 1 """
        form = BookingForm()
        self.assertEqual(form['num_adults'].initial, 1)

    def test_children_default_is_zero(self):
        """Check number of children field is initially set to 0 """
        form = BookingForm()
        self.assertEqual(form['num_children'].initial, 0)
