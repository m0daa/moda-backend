from ninja import Router
from ninja_jwt.authentication import JWTAuth

from user.schemas import LikedCurationSchema

router = Router(auth=JWTAuth())


@router.get("/")
def get_user(request):
    user = request.user
    return {"email": user.email, "name": user.name, "date_joined": user.date_joined}


@router.get("/liked/curation/")
def get_liked_curation_from_user(request):
    user = request.user
    liked_curations = user.likes.select_related("curation").prefetch_related(
        "curation__seasons", "curation__colors", "curation__products"
    )

    return [
        LikedCurationSchema.from_django_orm(like.curation) for like in liked_curations
    ]
