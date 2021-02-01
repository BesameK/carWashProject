from django.contrib import admin

from car_wash.models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ("id","carType","carModel","carYear")


class WasherAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","percent")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","price","order_date","end_date")


admin.site.register(Washer,WasherAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Order,OrderAdmin)

