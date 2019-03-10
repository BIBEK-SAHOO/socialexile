from django.db import models

class DownVote(models.Model):
    post_id = models.TextField()
    user_profile = models.TextField()
    def __str__(self):
        return "{0} - {1}".format(self.post_id, self.user_profile)
class Meta:
        unique_together = ["post_id", "user_profile"]

