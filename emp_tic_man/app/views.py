from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.


class CreateTicket(LoginRequiredMixin,CreateView):
    model = ticket
    # fields = ('summary','description')  # don't use this if form_class is there
    form_class=TicketAddForm
    template_name = 'app/add_ticket.html'
    success_url = reverse_lazy('all_tickets')

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ListTicket(LoginRequiredMixin,ListView):
    model = ticket
    template_name='app/ticket_list.html'


class DetailTicket(LoginRequiredMixin,DetailView):
    model = ticket
    template_name='app/show_ticket.html'
    context_object_name = 'ticket'
    

class UpdateTicket(LoginRequiredMixin,UpdateView):
    model = ticket
    form_class = TicketUpdateForm
    template_name='app/upd_ticket.html'
    success_url = reverse_lazy('all_tickets')

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs) 
        context['object']=self.object
        return context
        

class DeleteTicket(LoginRequiredMixin,DeleteView):
    model = ticket
    success_url = reverse_lazy('all_tickets')

