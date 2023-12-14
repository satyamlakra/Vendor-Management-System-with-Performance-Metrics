from django.db import models
from django.utils import timezone
# Create your models here.
class VendorProfileManagement(models.Model):
    name=models.CharField(max_length=125, null =False ,blank=False)
    contact_details=models.TextField()
    address= models.TextField()
    vendor_code=models.CharField(max_length=125, null =False ,blank=False,unique=True)
    on_time_delivery_rate=models.FloatField(null=True,blank=True)
    quality_rating_avg=models.FloatField(null=True,blank=True)
    average_response_time=models.FloatField(null=True,blank=True)
    fulfillment_rate=models.FloatField(null=True,blank=True)
    
class po(models.Model):
    choice=(("pending", "pending"), ("completed","completed"), ("canceled","canceled"))
    po_number= models.CharField(max_length=125) 
    vendor= models.ForeignKey(VendorProfileManagement,on_delete=models.CASCADE) 
    order_date= models.DateTimeField() 
    delivery_date= models.DateTimeField() 
    items= models.JSONField() 
    quantity= models.IntegerField()
    status= models.CharField(max_length=125,choices=choice)
    quality_rating= models.FloatField() 
    issue_date= models.DateTimeField()
    acknowledgment_date= models.DateTimeField(null=True,blank=True)
    
        
class Historical(models.Model):

    vendor= models.ForeignKey(VendorProfileManagement,on_delete=models.CASCADE)
    date= models.DateTimeField() 
    on_time_delivery_rate= models.FloatField() 
    quality_rating_avg= models.FloatField() 
    average_response_time= models.FloatField() 
    fulfillment_rate= models.FloatField()    
    def save(self, *args, **kwargs):
        
        
        self.date = timezone.now()
        return super(Historical, self).save(*args, **kwargs)