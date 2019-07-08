from django.contrib import admin
from django.urls import path, include
from .views import ReservationView, TableView, ReservationsListView, ReservationDetailView

app_name = 'table reservation'
urlpatterns = [
    path('reservation/create/', ReservationView.as_view()),
    path('table/create/', TableView.as_view()),
    path('reservations/', ReservationsListView.as_view()),
    path('reservations/detail/<int:pk>', ReservationDetailView.as_view())
]
