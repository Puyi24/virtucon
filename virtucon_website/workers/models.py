from django.db import models
from django.core.exceptions import ValidationError


class Job(models.Model):
    job_name = models.CharField(max_length=255)

    def __str__(self):
        return self.job_name


class Department(models.Model):
    dep_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dep_name


class Worker(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    professional_name = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(default="")
    job = models.ForeignKey(Job, default="Confidential", on_delete=models.SET_DEFAULT)
    department = models.ForeignKey(Department, default="General", on_delete=models.SET_DEFAULT)
    team_members = models.ManyToManyField('self', blank=True)
    manager = models.ForeignKey('self', null=True, default=None, on_delete=models.SET_DEFAULT)
    salary = models.IntegerField()
    hire_date = models.DateField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=7, unique=True)

    def __str__(self):
        if self.professional_name:
            return self.professional_name
        else:
            return f'{self.first_name} {self.last_name}'

    def clean(self):
        if not self.phone.isdigit() or len(self.phone) != 7:
            raise ValidationError({'phone': 'Phone number is consistent of exactly 7 numbers only'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
