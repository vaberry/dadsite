from django.db import models
from django.utils import timezone

# Create your models here.
class StoryModel(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    relationship = models.CharField(max_length=80, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)