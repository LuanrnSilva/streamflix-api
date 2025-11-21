from django.db import models
from django.contrib.auth.models import User


class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=400, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.CharField(max_length=10, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "tmdb_id")

    def __str__(self):
        return f"{self.user.email} - {self.title}"
