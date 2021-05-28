from django.contrib import admin
from .models import student_model, projects, blood_model,subjects,employee_model,company,assing

# Register your models here.
admin.site.register(student_model)
admin.site.register(projects)
admin.site.register(blood_model)
admin.site.register(subjects)
admin.site.register(employee_model)
admin.site.register(company)
admin.site.register(assing)
