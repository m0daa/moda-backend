from typing import List, Dict
from pydantic import BaseModel


class CurationSchema(BaseModel):
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
                "seasons": [season.name for season in obj.seasons.all()],
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
                "likes": obj.like_count,
                "created_at": obj.created_at.isoformat(),
            }
        )

    @classmethod
    def from_queryset(cls, queryset):
        return [cls.from_django_orm(obj) for obj in queryset]
