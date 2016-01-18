from django.contrib import admin

# Register your models here.
from .models import JobCategory, Job, JobApplication

admin.site.register(JobCategory)
admin.site.register(Job)
admin.site.register(JobApplication)
