# SmartEvent Phase 2

Starter implementation for:
- JWT authentication
- USER / ORGANIZER / ADMIN roles
- Organizer event management
- Organizer analytics
- Admin analytics
- Event lifecycle status

## Backend
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

API docs: http://127.0.0.1:8000/docs

## Frontend
cd frontend
npm install
npm run dev

The frontend is a simple React/Vite starter for connecting to the FastAPI APIs.
