from django.test import TestCase, Client
from django.urls import reverse
from dts_app.models import Note
from django.utils import timezone
import datetime


class ListNotesViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("dts_app:list_notes")

        # Create sample notes
        self.note1 = Note.objects.create(
            title="Note 1",
            description="Description 1",
            status=False,
            due_date_time=timezone.now() + datetime.timedelta(days=1)
        )
        self.note2 = Note.objects.create(
            title="Note 2",
            description="Description 2",
            status=True,
            due_date_time=timezone.now() + datetime.timedelta(days=2)
        )

    def test_list_notes_success(self):
        """Ensure all notes are returned successfully."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("notes", data)
        self.assertEqual(len(data["notes"]), 2)

        # Check structure of first note
        note_data = data["notes"][0]
        self.assertIn("id", note_data)
        self.assertIn("title", note_data)
        self.assertIn("description", note_data)
        self.assertIn("status", note_data)
        self.assertIn("due_date_time", note_data)
        self.assertIn("created_at", note_data)

    def test_list_notes_empty(self):
        """Ensure empty list is returned when there are no notes."""
        Note.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["notes"], [])

    def test_method_not_allowed(self):
        """Ensure non-GET requests return 400 error."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "GET method required")
