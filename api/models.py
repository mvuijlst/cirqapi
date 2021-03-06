from django.db import models

class Visitor(models.Model):
    rfid = models.CharField(max_length=255, blank=False, unique=True)
    fullname = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.rfid)