from django.db.models.signals import post_save
# from django.db.models.fil/
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from intro.models import  VendorProfileManagement,po,Historical
from django.db.models import  F, ExpressionWrapper, fields, Avg

@receiver(post_save,sender=po,dispatch_uid='at_ending_save')
def at_ending_save(sender, instance, created, **kwargs):
    
        divide=  len(po.objects.filter(vendor=instance.vendor,status='pending'))
        if  divide==0:
            divide=1
        qra=  sum(po.objects.filter(vendor=instance.vendor,status='completed').values_list('quality_rating', flat=True))/divide
        fr =  len(po.objects.filter(vendor=instance.vendor,status='completed'))/divide
        odr=  len(po.objects.filter(vendor=instance.vendor,delivery_date__lt= instance.delivery_date,status='completed'))/divide
        average_time_diff = po.objects.filter(vendor=instance.vendor).aggregate(
        average_completion=Avg(
            ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField()
            )
        )
    )
        
        data=instance.vendor
       
        data.quality_rating_avg= qra
        data.fulfillment_rate=fr
        data.on_time_delivery_rate=odr
        data.average_response_time=average_time_diff['average_completion'].total_seconds() / 3600
        data.save()
        Historical.objects.create(vendor=instance.vendor,on_time_delivery_rate= odr,
                                quality_rating_avg=qra, 
                                average_response_time= average_time_diff['average_completion'].total_seconds() / 3600, 
                                fulfillment_rate= fr,    ).save()

        
        






 