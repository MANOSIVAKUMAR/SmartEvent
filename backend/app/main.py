from fastapi import FastAPI
from app.routers import auth, events, organizer, admin

app = FastAPI(title="SmartEvent Phase 2 API", version="2.0.0")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(organizer.router, prefix="/api/organizer", tags=["Organizer"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "SmartEvent Phase 2 API is running"}
