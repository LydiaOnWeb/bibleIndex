from django.contrib import admin

from .models import Person
from .models import Relationship

# Register your models here.
admin.site.register(Person)
admin.site.register(Relationship)
