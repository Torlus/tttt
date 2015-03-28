from django.db import models

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('created_at',)

