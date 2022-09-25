import datetime
from django.db.models import Q
from django_cron import CronJobBase, Schedule
from .models import Customer


class MyCronJob(CronJobBase):

    schedule = Schedule(run_every_mins=1)
    code = 'cron.MyCronJob'

    def do(self):
        today = datetime.datetime.now()
        queryset = Customer.objects.filter(
            is_active=True, expire_date__year=today.year, expire_date__month=today.month, expire_date__day=today.day, expire_date__hour=today.hour, expire_date__minute=today.minute, expire_date__second=today.second).all()
        if not queryset is None:
            for item in queryset:
                customer_date = Customer.objects.get(pk=item.id)
                customer_date.is_active = False
                customer_date.save()
                print("Success")
        else:
            print("Not Avaliable Customer")
