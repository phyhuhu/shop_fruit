from django.contrib import admin
from .models import CreateQModel, CreateTaskModel

# Register your models here.

admin.site.register(CreateQModel)
admin.site.register(CreateTaskModel)