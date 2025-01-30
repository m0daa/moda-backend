from typing import List

from ninja import Router
from ninja_jwt.authentication import JWTAuth

from .models import Curation
from .schemas import CurationSchema

router = Router()


@router.get("/", auth=JWTAuth(), response=List[CurationSchema])
def get_curations(request, limit: int = 10):
    curations = Curation.objects.order_by("-created_at")[:limit]
    return [CurationSchema.from_orm(curation) for curation in curations]
