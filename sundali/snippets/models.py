from django.db import models

POINT_TYPE_CHOICES = (
    ('D', 'Depot'),
    ('L', 'Location'),
)


class Vehicle(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=100, blank=True, default='')
    machine_type = models.CharField(max_length=100, blank=True, default='')
    readiness = models.CharField(max_length=100, blank=True, default='')

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
    itinerary_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    point_id = models.ForeignKey(MainGraph, on_delete=models.CASCADE)
    order_num = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('itinerary_id',)
