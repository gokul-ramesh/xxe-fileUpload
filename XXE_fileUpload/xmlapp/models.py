from django.db import models

class XMLData(models.Model):
    title = models.CharField(max_length=255)
    xml_file = models.FileField(upload_to='xml_files/')
