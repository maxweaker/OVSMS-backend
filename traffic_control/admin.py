from django.contrib import admin

from .models import Car,Line,Frequency,RideRecord,Stop
# Register your models here.

admin.site.register(Car)
admin.site.register(Line)
admin.site.register(Frequency)
admin.site.register(RideRecord)
admin.site.register(Stop)