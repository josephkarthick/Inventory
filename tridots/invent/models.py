from django.db import models

class product(models.Model):
    product_id=models.CharField(max_length=50)
    
class location(models.Model):
    location_id = models.CharField(max_length=50)        
        
class productmovement(models.Model):
        movement_id = models.CharField(max_length=50)
        timestamp = models.DateTimeField(auto_now_add=True)
        from_location = models.CharField(max_length=50)
        to_location = models.CharField(max_length=50)
        Product_id = models.ForeignKey(product, on_delete = models.CASCADE)
        location = models.ForeignKey(location, on_delete = models.CASCADE)
        qyt = models.CharField(max_length=50)
      
