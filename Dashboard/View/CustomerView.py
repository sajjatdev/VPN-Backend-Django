from datetime import date, datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..models import Customer, Membership
from ..forms import CustomerForm


def CustomerList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        if current_user.is_admin == True:
            customerList = Customer.objects.all()
            return render(request, 'customer/CustomerList.html', context={'User_data': userdata, 'CustomerList': customerList})
        else:
            customerList = User.objects.filter(createby=current_user.id).all()
            return render(request, 'customer/CustomerList.html', context={'User_data': userdata, 'CustomerList': customerList})

    else:
        return redirect('/login/')


def CustomerCreate(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        m_querySet = Membership.objects.all()
        now = datetime.now()
        if request.method == "POST":
            name = request.POST['name']
            username = request.POST['username']
            password = request.POST['password']
            membership = request.POST['membership']
            print(membership)
            duration_count = Membership.objects.get(pk=membership)
            if not Customer.objects.filter(username=username).exists():
                if duration_count.name == "Month":
                    user_model = Customer.objects.create(name=name, username=username, password=password,
                                                         reseller_id=current_user.id, membership_id=membership, expire_date=(now+timedelta(days=30*int(duration_count.duration), hours=now.hour, minutes=now.minute, seconds=now.second)).isoformat())
                    user_model.save()
                    return redirect('/customerlist/')
                elif duration_count.name == "Years":
                    user_model = Customer.objects.create(name=name, username=username, password=password,
                                                         reseller_id=current_user.id, membership_id=membership, expire_date=(now+timedelta(days=365 * int(duration_count.duration), hours=now.hour, minutes=now.minute, seconds=now.second)).isoformat())
                    user_model.save()
                    return redirect('/customerlist/')
                elif duration_count.name == "Day":
                    user_model = Customer.objects.create(name=name, username=username, password=password,
                                                         reseller_id=current_user.id, membership_id=membership, expire_date=(now+timedelta(days=int(duration_count.duration), hours=now.hour, minutes=now.minute, seconds=now.second)).isoformat())
                    user_model.save()
                    return redirect('/customerlist/')
                else:

                    formdata = CustomerForm()
                    return render(request, 'customer/Customeradd.html', context={'User_data': userdata, 'forms': formdata, 'error': ''})

            else:
                return render(request, 'customer/Customeradd.html', context={'User_data': userdata, 'm_query': list(m_querySet), 'error': 'username'})

        else:
            return render(request, 'customer/Customeradd.html', context={'User_data': userdata, 'm_query': list(m_querySet), 'error': ''})

    else:
        return redirect('/login/')

 #      duration_count = str(
        #          form.cleaned_data['membership']).split(' ')
