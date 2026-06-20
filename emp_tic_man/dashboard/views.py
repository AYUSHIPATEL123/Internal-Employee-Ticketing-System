from django.shortcuts import render
from app.models import ticket
from authentication.models import CustomUser
from django.db.models import Value,Case,When,IntegerField,Count,Q
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

    tickets = ticket.objects.annotate(priority_order=Case(
        When(priority="HIGH",then=Value(1)),
        When(priority="MEDIUM",then=Value(2)),
        When(priority="LOW",then=Value(3)),
        default=Value(4),
        output_field= IntegerField() 
        ),
        status_order = Case(
            When(status="OPEN",then=Value(1)),
            When(status="IN-PROCESS",then=Value(2)),
            When(status="CLOSED",then=Value(3)),
            default=Value(4),
            output_field= IntegerField()
        )
    )

    open_tic_count = len(tickets.filter(status="OPEN"))
    inpro_tic_count = len(tickets.filter(status="IN-PROCESS"))
    res_tic_count = len(tickets.filter(status="CLOSED"))
    high_pri_count = len(tickets.filter(priority="HIGH"))

    all_tickets = tickets.order_by('status_order','priority_order','created_at')

    it_staff = CustomUser.objects.filter(role="IT-STAFF").prefetch_related('assignee_tickets').annotate(inp_count=Count('assignee_tickets',filter=Q(assignee_tickets__status="IN-PROCESS")) 
    ,res_count=Count('assignee_tickets'
    ,filter=Q(assignee_tickets__status="CLOSED")))

    # .annotate(total_tickets=Count("assignee_tickets")).filter(assignee_tickets__status="IN-PROCESS").annotate(inprocess_count=Count('assignee_tickets'))

    # print(it_staff[0].inprocess_count)    

    context={

        "open_tickets":open_tic_count,
        "inp_tickets":inpro_tic_count,
        "resoved_tickets":res_tic_count,
        "hi_pri_tickets":high_pri_count,
        "tickets":all_tickets,
        "it_staff":it_staff

    }

    return render(request,'dashboard/man_dashboard.html',context=context)