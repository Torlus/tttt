from django.db import models


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
    category = models.ForeignKey(Category)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return str(self.category) + " / [" + self.code + ": " + self.title + "]"

    class Meta:
        ordering = ('created_at',)


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return str(self.project) + " / [" + self.code + ": " + self.title + "]"

    class Meta:
        ordering = ('created_at',)
