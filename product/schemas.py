from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    category: str
    price: int
    image_url: str
    category: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def from_django_orm(cls, obj):
        data = {
            "id": obj.id,
            "name": obj.name,
            "price": obj.price,
            "image_url": obj.image_url,
            "category": obj.category,
        }
        return cls.model_validate(data)

    @classmethod
    def from_queryset(cls, queryset):
        return [cls.from_django_orm(obj) for obj in queryset]
