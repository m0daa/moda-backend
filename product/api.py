from typing import Optional

from ninja import Router
from ninja_jwt.authentication import JWTAuth

from product.models import Product
from product.schemas import ProductSchema

router = Router(auth=JWTAuth)


@router.get("/")
def get_products(request, category: Optional[str] = None, limit: int = 10):
    if category is None:
        products = Product.objects.all()[:limit]
    else:
        products = Product.objects.filter(category=category)[:limit]

    return ProductSchema.from_queryset(products)
