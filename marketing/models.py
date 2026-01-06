from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=120)
    org = models.CharField("Organization", max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=80, blank=True)
    use_case = models.CharField(max_length=160, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} - {self.org}"
