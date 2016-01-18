from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
JOB_TYPES = (
    ('FP', 'FixedPrice'),
    ('FT', 'Fulltime'),
    ('PT', 'Parttime'),
    ('HR', 'Hourly'),
)


class JobCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(JobCategory, related_name="category")
    skills = models.CharField(max_length=200)
    years_of_experience = models.CharField(max_length=60)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    duration = models.CharField(max_length=60)
    salary = models.CharField(max_length=60)
    details = models.TextField()
    location = models.CharField(max_length=200)
    date_created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    resume = models.FileField(upload_to="static/resume", max_length=20000)
    video = models.FileField(upload_to="static/video")

    def __str__(self):
        return self.name
