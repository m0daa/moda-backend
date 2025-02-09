from ninja import Router
from ninja_jwt.authentication import JWTAuth

router = Router(auth=JWTAuth())


@router.get("/")
def get_user(request):
    user = request.user
    return {"email": user.email, "name": user.name, "date_joined": user.date_joined}
