from django.contrib import admin
from intro.models import VendorProfileManagement,po,Historical
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
# Register your models here.
admin.site.register(VendorProfileManagement)
admin.site.register(po)
admin.site.register(Historical)