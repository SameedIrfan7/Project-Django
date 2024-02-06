from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique = False)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    
    #this function returns the value of what it has returned in the dailog box or table of database
    def __str__(self):
        return self.name