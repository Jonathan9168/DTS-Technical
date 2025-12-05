# DTS Developer Technical Test — Technical Test Solution

This project implements a simple task-creation system as required .

It consists of:

- **Backend:** Django API for task creation
- **Frontend:** Vue.js SPA for submitting tasks and displaying success/error messages

Only **task creation** is implemented, as per the specification.

---

## 📁 Project Structure

```
project-root/
│
├── dts/                 # Django project
│   ├── dts/             # Django settings
│   ├── dts_app/         # App containing Note/Task model + views
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/            # Vue.js application
    ├── src/
    ├── package.json
    └── vite.config.js
```

# 🚀 Backend Setup (Django)
## In directory with venv

```bash
cd dts
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Build DB

```bash
python manage.py migrate
```

## Start server

```bash
python manage.py runserver
```

## Run unit tests
```bash
python manage.py test dts_app
```

## The API will be available at:

```
http://127.0.0.1:8000/dts_app/notes/<create/list>
```

## 📌 API Endpoints

# Create Task

## POST /notes/create/

JSON Body Example

```json
{
  "title": "My task",
  "description": "Optional description",
  "status": false,
  "due_date_time": "2025-01-20T12:00:00Z"
}
```

Successful Response Example

```json
{
  "id": 1,
  "title": "My task",
  "description": "Optional description",
  "status": false,
  "due_date_time": "2025-01-20T12:00:00Z",
  "created_at": "2025-01-01T10:00:00Z"
}
```

## POST /notes/list/

```json
{
  "notes": [
    {
      "id": 1,
      "title": "Test Note",
      "description": "Testing",
      "status": false,
      "due_date_time": "2025-01-20T12:00:00+00:00",
      "created_at": "2025-11-28T18:37:59.834691+00:00"
    },
    {
      "id": 2,
      "title": "Test 2",
      "description": "Make a phone call",
      "status": false,
      "due_date_time": "2025-11-29T00:30:00+00:00",
      "created_at": "2025-11-28T22:28:46.759804+00:00"
    },
    {
      "id": 3,
      "title": "tedsaf",
      "description": "dsfsfdsf",
      "status": false,
      "due_date_time": "2025-11-29T22:31:00+00:00",
      "created_at": "2025-11-28T22:31:09.551119+00:00"
    },
    {
      "id": 4,
      "title": "wae",
      "description": "awe",
      "status": false,
      "due_date_time": "2025-12-06T22:34:00+00:00",
      "created_at": "2025-11-28T22:34:03.872602+00:00"
    },
    {
      "id": 5,
      "title": "Done",
      "description": "done",
      "status": true,
      "due_date_time": "2025-11-28T00:36:00+00:00",
      "created_at": "2025-11-28T22:37:01.228602+00:00"
    },
    {
      "id": 6,
      "title": "asdasdsaads",
      "description": "",
      "status": false,
      "due_date_time": "2026-01-02T22:51:00+00:00",
      "created_at": "2025-11-28T22:51:09.937801+00:00"
    }
  ]
}
```


# 🌐 Frontend Setup (Vue.js)

## Install dependencies

```bash
cd frontend
npm install
```

## Start dev server

```bash
npm run dev
```

## The app will be available at:

```bash
http://localhost:5173/
```
