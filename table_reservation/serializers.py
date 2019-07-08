from rest_framework import serializers
from .models import Reservation, Table


class ReservationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class TableDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('start_time', 'end_time', 'table')
