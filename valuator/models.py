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