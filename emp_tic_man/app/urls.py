from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('add_ticket/', CreateTicket.as_view(),name="add_ticket"),
    path('all_tickets/', ListTicket.as_view(),name="all_tickets"),
    path('upd_ticket/<int:pk>/', UpdateTicket.as_view(),name="upd_ticket"),
    path('show_ticket/<int:pk>/',DetailTicket.as_view(),name="ticket_detail"),
    path('del_ticket/<int:pk>/',DeleteTicket.as_view(),name="del_ticket"),
]