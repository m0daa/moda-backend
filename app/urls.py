from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from authentication.api import router as auth_router
from user.api import router as user_router
from curation.api import router as curation_router
from search.api import router as search_router
from product.api import router as product_router

api = NinjaAPI()

api.add_router("auth/", auth_router)
api.add_router("user/", user_router)
api.add_router("curation/", curation_router)
api.add_router("search/", search_router)
api.add_router("product/", product_router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]
