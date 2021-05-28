from django.contrib import admin
from .models import department_model, employee_model,student,projects

# Register your models here.
admin.site.register(employee_model)
admin.site.register(department_model)
admin.site.register(student)
admin.site.register(projects)
