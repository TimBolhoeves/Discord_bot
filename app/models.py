from django.db import models
from django.urls import reverse

class DiscordBot(models.Model):
    running = models.BooleanField()
    updated_at = models.DateField()
    
    def __str__(self):
        return self.running
    
    def get_absolute_url(self):
        return reverse("discordbot_detail", kwargs={"pk": self.pk})
