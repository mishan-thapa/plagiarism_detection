from django.contrib import admin

# Register your models here.
from .models import files, tfiles
admin.site.register(files)
admin.site.register(tfiles)