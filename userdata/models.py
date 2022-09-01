from django.db import models

# Create your models here.
class userData(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)


    def __str___(self):
        return self.name