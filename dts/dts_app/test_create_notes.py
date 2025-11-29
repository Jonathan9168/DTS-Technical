from django.test import TestCase, Client
from django.urls import reverse
import json
from dts_app.models import Note


class CreateNoteViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("dts_app:create_note")
        self.valid_payload = {
            "title": "Test Note",
            "description": "Test description",
            "status": False,
            "due_date_time": "2025-01-20T12:00:00Z"
        }

    def test_create_note_success(self):
        """Ensure a note is successfully created."""
        response = self.client.post(
            self.url,
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

        data = response.json()

        self.assertIn("id", data)
        self.assertEqual(data["title"], self.valid_payload["title"])
        self.assertEqual(data["description"], self.valid_payload["description"])
        self.assertEqual(data["status"], self.valid_payload["status"])
        self.assertEqual(data["due_date_time"], self.valid_payload["due_date_time"])

        # Check DB record exists
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.first()
        self.assertEqual(note.title, "Test Note")

    def test_missing_title_or_description(self):
        """Ensure missing title field returns 400."""
        invalid_payload = {
            "title": "",
            "description": "jhgv",
            "status": False
        }

        response = self.client.post(
            self.url,
            data=json.dumps(invalid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Title is required")

    def test_invalid_json(self):
        """Ensure invalid JSON returns 400 error."""
        response = self.client.post(
            self.url,
            data="not-json",
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Invalid JSON")

    def test_method_not_allowed(self):
        """Ensure GET request returns method error."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "POST method required")
