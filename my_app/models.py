# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EMPLOYEE(models.Model):
    fname = models.CharField(max_length=20)
    minit = models.CharField(max_length=1)
    lname = models.CharField(max_length=20)
    bdate = models.DateField()
    address = models.CharField(max_length=50)
    ssn = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=1,choices=(('F','Female'),('M','Male')))
    salary = models.IntegerField()
    super_ssn = models.IntegerField()
    dno = models.IntegerField()


    def __unicode__(self):
        return "%s" %self.name

class DEPARTMENT(models.Model):
    dname = models.CharField(max_length=20)
    dnumber = models.IntegerField(primary_key = True)
    mgr_ssn = models.IntegerField()
    mgr_start_date = models.DateField()

class DEPT_LOCATION(models.Model):
    dnumber = models.IntegerField(primary_key = True)
    dlocation = models.CharField(max_length=20)

class PROJECT(models.Model):
    pname = models.CharField(max_length=20)
    pnumber = models.IntegerField(primary_key = True)
    plocation = models.CharField(max_length=20)
    dnum = models.IntegerField()

class WORKS_ON(models.Model):
    essn = models.IntegerField(primary_key = True)
    pno = models.IntegerField()
    hours = models.FloatField()

class DEPENDENT(models.Model):
    essn = models.IntegerField(primary_key = True)
    dependent_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=(('F', 'Female'), ('M', 'Male')))
    bdate = models.DateField()
    relationship = models.CharField(max_length=20)
