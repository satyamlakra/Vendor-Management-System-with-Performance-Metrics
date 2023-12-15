from django.db.models.signals import post_save ,pre_save
# from django.db.models.fil/
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from intro.models import  VendorProfileManagement,po,Historical
from django.db.models import  F, ExpressionWrapper, fields, Avg
from django.utils import timezone


@receiver(post_save,sender=po,dispatch_uid='at_ending_save')
def at_ending_save(sender, instance, created, **kwargs):
    
        divide=  po.objects.filter(vendor=instance.vendor,status='pending').count()
        
        if  divide==0:
            divide=1
          
        qra= po.objects.filter(vendor=instance.vendor,status='completed').aggregate(Avg('quality_rating'))
        
        fr =  po.objects.filter(vendor=instance.vendor,status='completed').count()/divide
        
       
        
        average_time_diff = po.objects.filter(vendor=instance.vendor).aggregate(
        
        average_completion=Avg(
            ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField()
            )
        )
    )
       
        data=instance.vendor
       
        data.quality_rating_avg= qra['quality_rating__avg']
        data.fulfillment_rate=fr
        
        data.average_response_time=average_time_diff['average_completion'].total_seconds() / 3600
        data.save()
        
        Historical.objects.create(vendor=instance.vendor,on_time_delivery_rate=data.on_time_delivery_rate,
                                quality_rating_avg=qra['quality_rating__avg'], 
                                average_response_time= average_time_diff['average_completion'].total_seconds() / 3600, 
                                fulfillment_rate= fr,    ).save()

        
        



@receiver(pre_save,sender=po,dispatch_uid='at_start_save')
def at_start_save(sender, instance, **kwargs):
            divide1=  po.objects.filter(vendor=instance.vendor,status='completed').count()
            
            old_intance=    po.objects.get(id=instance.id)
            if old_intance.status=="pending" and instance.status=='completed':
                odr=  (po.objects.filter(vendor=instance.vendor,delivery_date__lt= timezone.now(),status='completed').count()+1)/(divide1+1)
                print(odr,divide1)
                data=instance.vendor
                data.on_time_delivery_rate=odr

                data.save() 
       