from django.contrib import admin
from .models import Company, CompanyUser, Applicant

admin.site.register(Company)
admin.site.register(CompanyUser)
admin.site.register(Applicant)
