from  rest_framework import serializers
from  intro.models import  VendorProfileManagement,po


from django.contrib.auth.models import User


class vpm(serializers.ModelSerializer):
    class Meta:
        model= VendorProfileManagement
        fields='__all__'
class pvpm(serializers.ModelSerializer):
    class Meta:
        model= VendorProfileManagement
        fields=["on_time_delivery_rate", "quality_rating_avg","average_response_time", "fulfillment_rate"]        
        
class poapi(serializers.ModelSerializer):
      class Meta:
            model= po
            fields='__all__'       


class apoapi(serializers.ModelSerializer):
    class Meta:
        model= po
        fields=['acknowledgment_date']            