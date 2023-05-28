from django.contrib import admin

from .models import apidata,money,accountactivity,splitbill
admin.site.register(apidata)
admin.site.register(money)
admin.site.register(accountactivity)
admin.site.register(splitbill)
# Register your models here.
