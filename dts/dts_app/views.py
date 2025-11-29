import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note


@csrf_exempt
def create_note(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    title = data.get("title")
    description = data.get("description")
    status = data.get("status", False)
    due_date_time = data.get("due_date_time")

    if not title:
        return JsonResponse({"error": "Title is required"}, status=400)

    note = Note.objects.create(
        title=title,
        description=description,
        status=status,
        due_date_time=due_date_time
    )

    return JsonResponse({
        "id": note.id,
        "title": note.title,
        "description": note.description,
        "status": note.status,
        "due_date_time": note.due_date_time,
        "created_at": note.created_at
    }, status=201)


@csrf_exempt
def list_notes(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET method required"}, status=400)

    notes = Note.objects.all().values(
        "id", "title", "description", "status", "due_date_time", "created_at"
    )

    notes_list = []
    for note in notes:
        notes_list.append({
            "id": note["id"],
            "title": note["title"],
            "description": note["description"],
            "status": note["status"],
            "due_date_time": note["due_date_time"].isoformat() if note["due_date_time"] else None,
            "created_at": note["created_at"].isoformat() if note["created_at"] else None,
        })

    return JsonResponse({"notes": notes_list}, status=200)