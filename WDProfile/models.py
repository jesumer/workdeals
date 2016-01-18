from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from WDJob.models import Job, JobApplication

COMPANY_USER_TYPES = (
    ('CO', 'CompanyOwner'),
    ('HRM', 'HumanResourceManager'),
)


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CompanyUser(models.Model):
    user = models.ForeignKey(User, related_name="company_user")
    company = models.ForeignKey(Company, related_name="company")
    user_type = models.CharField(max_length=200, choices=COMPANY_USER_TYPES)
    job = models.ForeignKey(Job, related_name='job')

    def __str__(self):
        return self.user_type


class Applicant(models.Model):
    user = models.ForeignKey(User, related_name="applicant_user")
    job_application = models.ForeignKey(JobApplication, related_name='job_application')
