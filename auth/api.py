import requests

from django.conf import settings

from ninja import Router
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import RefreshToken

router = Router()


@router.get("/kakao/login/")
def kakao_login(request):
    kakao_auth_url = (
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={settings.KAKAO_CLIENT_ID}"
        f"&redirect_uri={settings.KAKAO_REDIRECT_URI}"
        f"&response_type=code"
    )
    return {"kakao_auth_url": kakao_auth_url}


@router.get("/kakao/callback/")
def kakao_callback(request, code: str):
    token_response = requests.post(
        settings.KAKAO_TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "client_id": settings.KAKAO_CLIENT_ID,
            "client_secret": settings.KAKAO_CLIENT_SECRET_ID,
            "redirect_uri": settings.KAKAO_REDIRECT_URI,
            "code": code,
        },
    )

    if token_response.status_code != 200:
        raise HttpError(
            status_code=401,
            message="Invalid authorization code or token request failed.",
        )

    token_json = token_response.json()
    access_token = token_json.get("access_token")

    if not access_token:
        raise HttpError(
            status_code=401,
            message="Access token not found.",
        )

    # 카카오 사용자 정보 요청
    user_response = requests.get(
        settings.KAKAO_USER_INFO_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()

    # 사용자 정보 확인
    kakao_id = user_info.get("id")
    kakao_email = user_info.get("kakao_account", {}).get("email")
    kakao_nickname = user_info.get("properties", {}).get("nickname")

    # 사용자 생성 또는 확인
    from django.contrib.auth.models import User

    user, created = User.objects.get_or_create(
        username=kakao_id,
        defaults={
            "email": kakao_email,
            "first_name": kakao_nickname,
        },
    )

    # JWT 발급
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@router.get("/protected-endpoint", auth=JWTAuth())
def protected_endpoint(request):
    user = request.user
    return {"message": f"hola, {request.user.first_name}"}
