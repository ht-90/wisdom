from django.test import TestCase

from ..forms import UploadFileForm


class TestUploadFileForm(TestCase):
    def test_invalid_form(self):
        """Test form to fail with unacceptable data field"""
        data = {
            "dummy_field": "test"
        }
        form = UploadFileForm(data=data)
        self.assertFalse(form.is_valid(), "Field not in metadata")
