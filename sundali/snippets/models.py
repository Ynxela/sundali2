from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


class Vehicle(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=100, blank=True, default='')
    machine_type = models.IntegerField()
    readiness = models.TextField(blank=True)

    class Meta:
        ordering = ('machine_id',)


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    machine_id = models.IntegerField()

    class Meta:
        ordering = ('task_id',)


class MainGraph(models.Model):
    point_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=100, blank=True, default='')
    machine_type = models.IntegerField()
    readiness = models.TextField(blank=True)

    class Meta:
        ordering = ('machine_id',)


