from fastapi import APIRouter
from src.booking_app.routers.book_router import router as booking_router

router = APIRouter(
    prefix="/books",
    tags=["Booking"]
)
router.include_router(booking_router)
