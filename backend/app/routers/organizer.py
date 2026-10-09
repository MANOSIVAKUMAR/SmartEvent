from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.dependencies import require_roles

router = APIRouter()

class EventCreate(BaseModel):
    title: str
    description: str = ""
    event_date: str
    venue: str
    total_tickets: int
    ticket_price: float

@router.post("/events")
def create_event(data: EventCreate, user=Depends(require_roles("ORGANIZER"))):
    return {
        "message": "Event created",
        "organizer_id": user["sub"],
        "event": data.model_dump()
    }

@router.get("/events")
def my_events(user=Depends(require_roles("ORGANIZER"))):
    return {"organizer_id": user["sub"], "events": []}

@router.put("/events/{event_id}")
def update_event(event_id: int, data: EventCreate, user=Depends(require_roles("ORGANIZER"))):
    return {"message": "Event updated", "event_id": event_id, "organizer_id": user["sub"]}

@router.patch("/events/{event_id}/cancel")
def cancel_event(event_id: int, user=Depends(require_roles("ORGANIZER"))):
    return {"message": "Event cancelled", "event_id": event_id}

@router.get("/events/{event_id}/bookings")
def event_bookings(event_id: int, user=Depends(require_roles("ORGANIZER"))):
    return {"event_id": event_id, "bookings": []}

@router.get("/analytics")
def organizer_analytics(user=Depends(require_roles("ORGANIZER"))):
    return {
        "total_tickets_sold": 0,
        "remaining_tickets": 0,
        "total_revenue": 0,
        "booking_count": 0,
        "events": []
    }
