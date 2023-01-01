from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FilesData(models.Model):
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    descreption=models.TextField(null=True,blank=True)
    create_datetime= models.DateTimeField(auto_now_add=True)
    document=models.FileField(upload_to='documents/',default=None)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['create_datetime']
