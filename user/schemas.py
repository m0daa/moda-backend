from typing import List, Dict
from pydantic import BaseModel


class LikedCurationSchema(BaseModel):
    id: int
    title: str
    seasons: List[str]
    colors: List[str]
    products: List[Dict[str, str]]
    likes: int
    created_at: str

    class Config:
        from_attributes = True

    @classmethod
    def from_django_orm(cls, obj):
        return cls.model_validate(
            {
                "id": obj.id,
                "title": obj.title,
                "seasons": list(obj.seasons.values_list("name", flat=True)),
                "colors": [color.name for color in obj.colors.all()],
                "products": [
                    {
                        "id": str(product.id),
                        "name": product.name,
                        "brand": product.brand,
                        "price": str(product.price),
                        "image_url": product.image_url,
                    }
                    for product in obj.products.all()
                ],
                "likes": obj.likes.count(),
                "created_at": obj.created_at.isoformat(),
            }
        )
