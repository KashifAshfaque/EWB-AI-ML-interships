
from fastapi import APIRouter

from routes import (
    create_students,
    get_students,
    update_students,
    delete_students,
    ai_query,
)

api_router = APIRouter()

api_router.include_router(create_students.router)
api_router.include_router(get_students.router)
api_router.include_router(update_students.router)
api_router.include_router(delete_students.router)
api_router.include_router(ai_query.router)
