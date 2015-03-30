from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return "[" + self.code + ": " + self.title + "]"

    class Meta:
        ordering = ('created_at',)


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return str(self.category) + " / [" + self.code + ": " + self.title + "]"

    class Meta:
        ordering = ('created_at',)


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return str(self.project) + " / [" + self.code + ": " + self.title + "]"

    class Meta:
        ordering = ('created_at',)


class Work(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='works')
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    units = models.IntegerField()

    class Meta:
        ordering = ('created_at',)