from django.db import models

class DownVote(models.Model):
    post_id = models.TextField()
    user_profile = models.TextField()
class Meta:
        unique_together = ["post_id", "user_profile"]

