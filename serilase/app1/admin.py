from django.contrib import admin

# Register your models here.
from app1.models import car

admin.site.register(car)


class caradmin(admin.ModelAdmin):
    disp = ['id', 'name', 'model', 'number']
