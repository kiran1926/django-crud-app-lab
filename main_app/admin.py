from django.contrib import admin
from .models import Plant, Watering, Fertilizer
# Register your models here.
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Fertilizer)
