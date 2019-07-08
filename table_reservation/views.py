from django.shortcuts import render
from rest_framework import generics
from .serializers import ReservationDetailSerializer, TableDetailSerializer, ReservationsSerializer
from .models import Reservation


class ReservationView(generics.CreateAPIView):
    serializer_class = ReservationDetailSerializer


class TableView(generics.CreateAPIView):
    serializer_class = TableDetailSerializer


class ReservationsListView(generics.ListAPIView):
    serializer_class = ReservationsSerializer
    queryset = Reservation.objects.all()


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationDetailSerializer
    queryset = Reservation.objects.all()
