from django.conf import settings
from django.db import models

from curation.models import Curation


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    curation = models.ForeignKey(
        Curation, on_delete=models.CASCADE, related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "curation")

    def __str__(self):
        return f"{self.user.first_name}님이 {self.curation.title}를 좋아합니다"
