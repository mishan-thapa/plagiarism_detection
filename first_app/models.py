from django.db import models

# Create your models here.
class files(models.Model):
    first_file = models.FileField(upload_to="files")
    second_file = models.FileField(upload_to="files")


class tfiles(models.Model):
    first_file = models.FileField(upload_to="files")
    second_file = models.FileField(upload_to="files")

class thesis_docx(models.Model):
    thesis = models.FileField(upload_to='thesis_files') # Uploaded files will be stored in the 'thesis_files/' directory inside MEDIA_ROOT