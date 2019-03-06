from django.db import models

# Create your models here.

class Follow(model.Model):
    uid=models.CharField()
    fid=models.CharField()
    
