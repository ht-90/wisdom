from django.test import TestCase, Client


class TestAudioUpload(TestCase):
    """Test audio upload view"""

    def test_request_audio_upload(self):
        """Test accessing audio upload url"""
        c = Client()
        response = c.post("/upload/", {"name": "test"})
        self.assertEqual(response.status_code, 200)


class TestSuccess(TestCase):
    """Test audio upload success view"""
    def test_request_audio_upload_success(self):
        """Test accessing audio upload success url"""
        c = Client()
        response = c.post("/success/", {"name": "test"})
        self.assertEqual(response.status_code, 200)
