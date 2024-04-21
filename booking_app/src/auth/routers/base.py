from fastapi import APIRouter
from src.auth.routers.user_router import router as user_router

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)
router.include_router(user_router)
