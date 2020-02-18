# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.CharField(max_length=20)
    NickName = models.TextField(max_length=30)

class UserPhone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userphone = models.CharField(max_length=30)