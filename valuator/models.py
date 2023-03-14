from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class SearchInput(models.Model):
    user_input = models.CharField(max_length=300)
    date_created = models.DateTimeField("date_search_input_by_user")

    def __str__(self):
        return self.user_input


class ActualBottle(models.Model):
    actual_bottle = models.CharField(max_length=300)
    photo_url = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField("date_actual_bottle_added_to_db")

    def __str__(self):
        return f"{self.actual_bottle} {self.date_created}"
    

class Post(models.Model):
    title = models.CharField(max_length=300)
    image_name = models.TextField()
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user} post_id: {self.post}"