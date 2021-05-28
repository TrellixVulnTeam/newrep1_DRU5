from django.contrib import admin
from .models import car_model, engine_model,department1,employee1

# Register your models here.
admin.site.register(car_model)
admin.site.register(engine_model)
# admin.site.register(d_epartment)
# admin.site.register(e_mployee)
admin.site.register(department1)
admin.site.register(employee1)

