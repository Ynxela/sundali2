from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
POINT_TYPE_CHOICES = (
    ('D', 'Depot'),
    ('L', 'Location'),
)


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
    machine_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    task_type_cd = models.CharField(max_length=100, blank=True, default='')
    task_status_cd = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('task_id',)


class MainGraph(models.Model):
    point_id = models.AutoField(primary_key=True)
    point_type = models.CharField(max_length=1, default='L', choices=POINT_TYPE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('point_id',)


class TaskPoints(models.Model):
    task_id = models.AutoField(primary_key=True)
    point_id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('task_id',)
