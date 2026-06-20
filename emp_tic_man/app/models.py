from django.db import models
from authentication.models import CustomUser
from django.utils import timezone
from django.urls import reverse
from .services import assign_priority
# Create your models here.


class ticket(models.Model):

    PRIORITIES = (
        ('LOW','low'),
        ('MEDIUM','medium'),
        ('HIGH','high'),
    )

    STATUSES=(
        ('OPEN','open'),
        ('IN-PROCESS','in process'),
        ('CLOSED','closed'),
    )

    summary = models.CharField(max_length=400)
    employee = models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'EMPLOYEE'},related_name='employee_tickets')
    assignee = models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'IT-STAFF'},related_name='assignee_tickets',null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUSES,default='OPEN')
    priority=models.CharField(max_length=100,choices=PRIORITIES,default='LOW')
    created_at = models.DateField(default=timezone.now)
    description=models.TextField(max_length=10000)
    resolved_at = models.DateField(null=True,blank=True)



    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})

    def save(self,*args,**kwargs):
        self.priority = assign_priority(self.description) 
        super().save(*args,**kwargs)  

    def __str__(self):
        return self.summary     
    
