from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from authentication.api import router as auth_router
from curation.api import router as curation_router

api = NinjaAPI()

api.add_router("auth/", auth_router)
api.add_router("curation/", curation_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]
