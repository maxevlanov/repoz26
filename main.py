from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints.v1 import api_v1_router
from endpoints.auth.api import auth_router

tags = [
    {
        "name": "Category",
        "description": "Endpoints for category"
    },
    {
        "name": "Product",
        "description": "Endpoints for product"
    },
    {
        "name": "BotUser",
        "description": "Endpoints for bot_user"
    },
    {
        "name": "Invoice",
        "description": "Endpoints for invoice"
    },
    {
        "name": "Language",
        "description": "Endpoints for language"
    },
    {
        "name": "OrderItem",
        "description": "Endpoints for order_item"
    },
    {
        "name": "Status",
        "description": "Endpoints for status"
    },
    {
        "name": "Order",
        "description": "Endpoints for order"
    }
]

app = FastAPI(
    title="Belhard",
    description="Belhard Lesson",
    version="0.0.1",
    openapi_tags=tags
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(api_v1_router)
app.include_router(auth_router)
