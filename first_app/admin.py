from django.contrib import admin

# Register your models here.
from .models import files, tfiles, thesis_docx
admin.site.register(files)
admin.site.register(tfiles)
admin.site.register(thesis_docx)