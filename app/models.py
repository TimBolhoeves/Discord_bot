from django.db import models
from django.urls import reverse

class DiscordBot(models.Model):
    name = models.CharField(max_length=255, null=True)
    running = models.BooleanField()
    updated_at = models.DateField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("discordbot_detail", kwargs={"pk": self.pk})
