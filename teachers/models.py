from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField()
    image = models.ImageField()
    file = models.FileField(upload_to ="classnotes")