from fastapi import APIRoutet
from store.controllers.product import router as product

api_router = APIRouter()
api_router.include(product, prefix="/products")