from django.test import TestCase
from django.db.utils import DataError

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

    def test_name_length(self):
        """Test excessive length of audio name"""
        excess_name = "a" * 51
        with self.assertRaises(DataError) as error_name:
            Audio.objects.create(name=excess_name)
        self.assertEqual(
            error_name.exception.__str__().strip("\n"),
            "value too long for type character varying(50)",
        )

    def test_description_length(self):
        """Test excessive length of audio description"""
        excess_desc = "a" * 201
        with self.assertRaises(DataError) as error_desc:
            Audio.objects.create(description=excess_desc)
        self.assertEqual(
            error_desc.exception.__str__().strip("\n"),
            "value too long for type character varying(200)",
        )
