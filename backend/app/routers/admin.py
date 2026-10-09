from fastapi import APIRouter, Depends
from app.dependencies import require_roles

router = APIRouter()

@router.get("/users")
def all_users(user=Depends(require_roles("ADMIN"))):
    return {"users": []}

@router.get("/events")
def all_events(user=Depends(require_roles("ADMIN"))):
    return {"events": []}

@router.get("/bookings")
def all_bookings(user=Depends(require_roles("ADMIN"))):
    return {"bookings": []}

@router.get("/analytics")
def analytics(user=Depends(require_roles("ADMIN"))):
    return {
        "total_registered_users": 0,
        "total_events_created": 0,
        "total_tickets_sold": 0,
        "total_bookings": 0,
        "platform_revenue": 0,
        "daily_ticket_sales": [],
        "monthly_booking_trends": [],
        "popular_events": [],
        "top_revenue_events": []
    }
