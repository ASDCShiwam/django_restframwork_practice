from django.db import models

class Students(models.Model):
    st_id=models.CharField(max_length=10)
    st_name=models.CharField(max_length=30)
    st_age=models.IntegerField()
    
    def __str__(self):
        return self.st_name

# Create your models here.
