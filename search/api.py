from ninja import Router
from ninja_jwt.authentication import JWTAuth

from product.models import Product

router = Router(auth=JWTAuth())


@router.get("/")
def search_products(request, query: str):
    products = Product.objects.filter(name__icontains=query)
    return {
        "results": list(products.values("id", "name", "brand", "price", "image_url"))
    }
