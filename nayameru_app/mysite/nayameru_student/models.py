from django.db import models
from userauth.models import CustomUser

# Create your models here.

class SearchLog(models.Model):
    user = models.ForeignKey(CustomUser,
                                on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    lowest_price = models.IntegerField()
    at_data = models.DateTimeField('date published')

    class Meta:
        abstract = True

