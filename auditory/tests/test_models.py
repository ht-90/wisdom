from django.test import TestCase, Client
from django.core.files import File

from ..models import Audio


class TestAudio(TestCase):
    """Testcase for auditory Audio model"""
    def setUp(self):
        """Create a test audio object"""
        Audio.objects.create(
            name="test_audio",
            description="",
            thumbnail="",
            audiofile="",
        )

    def test_name_field(self):
        """Test object name register"""
        audio = Audio.objects.get(name="test_audio")
        self.assertEqual(audio.__str__(), "test_audio")
