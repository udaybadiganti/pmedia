from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class district(models.Model):
    district_ident = models.CharField(max_length = 10)
    district_name = models.CharField(max_length = 50)
    district_logo = models.CharField(max_length = 1000)
    district_pincode = models.CharField(max_length = 6)

    def __str__(self):
        return self.district_name

class assemblies(models.Model):
    districts = models.ForeignKey(district, on_delete=models.CASCADE)
    assembly = models.CharField(max_length = 20)
    assembly_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.assembly


class public_complaints(models.Model):
    complaint = models.ForeignKey(assemblies, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='post_complain', null = True)
    created_on = models.DateTimeField(auto_now_add=True, null = True)
    complaint_type = models.CharField(max_length = 20)
    complaint_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 10000)
    complaint_photo = models.ImageField(upload_to = 'images/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.complaint_name
