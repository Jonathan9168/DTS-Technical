from django.urls import path
from . import views

""""
    Invoke-RestMethod -Method Post `
    -Uri "http://127.0.0.1:8000/dts_app/notes/create/" `
    -ContentType "application/json" `
    -Body '{"title":"Test Note","description":"Testing","status":false,"due_date_time":"2025-01-20T12:00:00Z"}'
"""

app_name = "dts_app"

urlpatterns = [
    path("notes/create/", views.create_note, name="create_note"),
    path("notes/list/", views.list_notes, name="list_notes")
]
