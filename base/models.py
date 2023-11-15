from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=200, null=True, blank=True)
    image= models.ImageField(null=True, blank=True, default='/placeholder.png')
    category= models.CharField(max_length=200, null=True, blank=True)
    description= models.TextField(null=True, blank=True)
    price= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank= True)
    createdAt= models.DateTimeField(auto_now_add=True)
    discount= models.BooleanField(default=False)
    percentage= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True) 
    endDate= models.DateField(null=True, blank=True) 
    discounted_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)  
    _id=models.AutoField(primary_key=True, editable=False)
    
    def save(self, *args, **kwargs):
        if self.discount and self.percentage is not None:
            self.discounted_price = float(self.price) - (float(self.price) * (float(self.percentage) / 100))
        else:
            self.discounted_price = None
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    


