from django.shortcuts import render
from app.models import ticket
from django.db.models import Value,Case,When,IntegerField
# Create your views here.


def staff(request):
    tickets = ticket.objects.annotate(priority_order=Case(
        When(priority="HIGH", then=Value(1)),
        When(priority="MEDIUM", then=Value(2)),
        When(priority="LOW", then=Value(3)),
        default=Value(4),
        output_field=IntegerField()
    ))

    open_tickets = tickets.filter(status="open").order_by('priority_order','created_at')
    open_tic_count = len(open_tickets)
    

    staff_tickets = tickets.filter(assignee=request.user,status="in-process").order_by('priority_order','created_at')

    staff_tic_count = len(staff_tickets)

    hi_pri_tic_count  = len(tickets.filter(assignee=request.user,priority="high"))

    re_tic_count = len(tickets.filter(assignee=request.user,status="closed"))

    context = {
        "open_tic_count":open_tic_count,
        "staff_tic_count":staff_tic_count,
        "high_pri_count":hi_pri_tic_count,
        "res_count":re_tic_count,
        "open_tickets":open_tickets,
        "staff_tickets":staff_tickets,
    }


    return render(request,'dashboard/it_stf_dashboard.html',context=context)


def manager(request):
    return render(request,'dashboard/man_dashboard.html')