from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Case,When,Value,IntegerField
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import *
from .forms import *
# Create your views here.


class CreateTicket(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = ticket
    # fields = ('summary','description')  # don't use this if form_class is there
    form_class = TicketAddForm
    permission_required = 'app.add_ticket'
    permission_denied_message = "you can not add these data"
    template_name = 'app/add_ticket.html'
    success_url = reverse_lazy('all_tickets')

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ListTicket(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    
    model = ticket
    permission_required = 'app.view_ticket'
    permission_denied_message = "you can not view these data"
    template_name='app/ticket_list.html'

    def get_queryset(self):

        tickets = ticket.objects.annotate(
            priority_order=Case(
                When(priority="high",then=Value(1)),
                When(priority="medium",then=Value(2)),
                When(priority="low",then=Value(3)),
                default=Value(4),
                output_field=IntegerField()
            ),
            status_order=Case(
                When(status="open",then=Value(1)),
                When(status="IN-PROCESS",then=Value(2)),
                When(status="closed",then=Value(3)),
                default=Value(4),
                output_field=IntegerField()
            )
        ).order_by("status_order","priority_order","date")


        user = self.request.user

        if user.role == 'EMPLOYEE':

            tickets = tickets.filter(employee=user)

        return tickets    




class DetailTicket(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = ticket
    permission_required = 'app.view_ticket'
    permission_denied_message = "you can not view these data"
    template_name='app/show_ticket.html'
    context_object_name = 'ticket'
    

class UpdateTicket(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = ticket
    form_class = TicketUpdateForm
    permission_required = 'app.change_ticket'
    permission_denied_message = "you do not have the permission to update data"
    template_name='app/upd_ticket.html'
    success_url = reverse_lazy('all_tickets')


    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs) 
        context['object']=self.object
        return context
        

class DeleteTicket(LoginRequiredMixin,DeleteView):
    model = ticket
    permission_required = 'app.delete_ticket'
    permission_denied_message = "you can not delete this data"
    success_url = reverse_lazy('all_tickets')

