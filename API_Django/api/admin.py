from django.contrib import admin
from  .models import api_data

class api_data_property(admin.ModelAdmin):
    list_display=['title','category','color','size']

admin.site.register(api_data,api_data_property)
