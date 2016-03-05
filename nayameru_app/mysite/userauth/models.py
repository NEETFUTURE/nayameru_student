from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    universityname = models.CharField(
        max_length=20,
        verbose_name="大学名",
        default=""
    )

    def __str__(self):
        return u"%s:%s:%s"%(self.username, self.universityname, self.email)
