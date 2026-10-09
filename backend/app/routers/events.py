from datetime import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.dependencies import get_current_user
from app.models import EventStatus

router = APIRouter()

class EventCreate(BaseModel):
    title: str
    description: str = ""
    event_date: datetime
    venue: str
    total_tickets: int
    ticket_price: float

@router.get("/")
def list_events():
    return {"message": "Public event list endpoint", "events": []}

@router.get("/{event_id}")
def get_event(event_id: int):
    return {"event_id": event_id, "message": "Event details endpoint"}

@router.post("/{event_id}/book")
def book_event(event_id: int, user=Depends(get_current_user)):
    return {"message": "Booking endpoint - connect to Phase 1 booking logic", "event_id": event_id, "user_id": user["sub"]}
