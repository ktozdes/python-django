from django.db import models

# Create your models here.

class Attachment(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    thumbnail_url = models.CharField(max_length=255,default=0, null=True)
    attachable_id = models.IntegerField(default=0, null=True)
    attachable_type = models.CharField(max_length=255, default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    class Meta:
	    indexes = [
	        models.Index(fields=['attachable_id'], name='attachement_attachable_id'),
	        models.Index(fields=['attachable_type'], name='attachement_attachable_type')
	    ]
