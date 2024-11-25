from fastapi import APIRouter

from src.api.v1.views import (api_user, chat_views, group_views)

router = APIRouter(prefix="/api/v1")

router.include_router(api_user.router, tags=["User Endpoints"])
router.include_router(chat_views.router, tags=["Chat Endpoints"])
router.include_router(group_views.router, tags=["Group Endpoints"])