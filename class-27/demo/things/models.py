from django.db import models
from django.contrib.auth import get_user_model

# This model represents a Thing
class Thing(models.Model):
    # name, rating, reviewer fields in our model
    name = models.CharField(max_length=128)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)


