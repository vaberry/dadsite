from django.db import models

# Create your models here.
class StoryModel(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)