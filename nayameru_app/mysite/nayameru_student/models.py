from django.db import models

# Create your models here.

class SearchLog(models.Model):
    user_name = models.ForeignKey("User",
                                on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    lowest_price = models.IntegerField()
    at_data = models.DateTimeField('date published')
    class Meta:
        abstract = True

