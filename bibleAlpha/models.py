# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Relationship(models.Model):
    person1 = models.ForeignKey(Person, related_name='subject_person', on_delete=models.CASCADE)
    relationshipOf = models.CharField(max_length=200)
    person2 = models.ForeignKey(Person, related_name='subject_object', on_delete=models.CASCADE)
    def __str__(self):
        return self.person1.name + u' 是 ' + self.person2.name + u' 的 ' + self.relationshipOf
