from django.test import TestCase, Client

from ..models import Audio


class TestAudioUpload(TestCase):
    """Test audio upload view"""

    def test_request_audio_upload(self):
        """Test accessing audio upload url"""
        c = Client()
        response = c.post("/upload/", {"name": "test"})
        self.assertEqual(response.status_code, 200)


class TestAuditoriumView(TestCase):
    """Test case for AuditoriumView"""

    def setUp(self):
        """Set up audio objects"""
        self.audio = Audio.objects.create(name="test_audio")
        self.audio_other = Audio.objects.create(name="test_audio_other")

    def test_request_audio_view(self):
        """Test parameterized auditorium url"""
        c = Client()
        response = c.get(f"/auditorium/{self.audio.uuid}", {"id": self.audio.uuid})
        self.assertEqual(response.status_code, 200)

    def test_get_queryset(self):
        """Test queryset for audio object"""
        c = Client()
        response = c.get(f"/auditorium/{self.audio.uuid}", {"id": self.audio.uuid})
        self.assertEqual(
            response.context["audio_list"].values()[0]["name"],
            self.audio.name,
        )

    def test_get_context_data(self):
        """Test creating context other_audio"""
        c = Client()
        response = c.get(f"/auditorium/{self.audio.uuid}", {"id": self.audio.uuid})
        self.assertEqual(
            response.context["other_audios"].values()[0]["name"],
            self.audio_other.name,
        )


class TestSuccess(TestCase):
    """Test audio upload success view"""
    def test_request_audio_upload_success(self):
        """Test accessing audio upload success url"""
        c = Client()
        response = c.post("/success/", {"name": "test"})
        self.assertEqual(response.status_code, 200)
