from django.db import models



# Create your models here.
class Product(models.Model):
    paper_id=models.AutoField
    paper_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=100)
    
    image=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.paper_name
    
## models.py
class Paper(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='papers/')
    category = models.CharField(max_length=50, choices=[
        ('MID-1', 'MID-1'),
        ('MID-2', 'MID-2'),
        ('SEM', 'SEM'),
        ('Others', 'Others'),
    ])
