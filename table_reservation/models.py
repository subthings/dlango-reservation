from django.db import models


class Reservation(models.Model):
    start_time = models.DateTimeField('start reservation time')
    end_time = models.DateTimeField('end reservation time')
    number_of_person = models.IntegerField()
    comment = models.CharField(max_length=300)
    reservation_name = models.CharField(max_length=100)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)


class Table(models.Model):
    table_number = models.IntegerField(unique=True, primary_key=True)
    table_capacity = models.IntegerField()
