from django.contrib.auth import get_user_model
from django.db import models

# Model for a blog post
class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # overriding toString() for more user friendly output 
    def __str__(self):
        return self.title
