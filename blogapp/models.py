from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.field_title