from random import choice
from string import digits, ascii_letters
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


def customerStatus(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            status = request.POST['status']
            now = datetime.now()
            data = get_object_or_404(Customer, pk=id)
            if status == "1":
                data.is_active = False
                data.save()

            else:

                # Expire Date add
                duration_count = Membership.objects.get(pk=data.membership.id)
                print(duration_count.name)
                if duration_count.name == "Month":
                    data.is_active = True
                    data.join_date = now
                    data.expire_date = (now+timedelta(days=30 * int(
                        duration_count.duration), hours=now.hour, minutes=now.minute, seconds=now.second)).isoformat()
                    data.save()
                    print("success")
                    return redirect('/customerlist/')
                elif duration_count.name == "Years":
                    user_model = Customer.objects.update(
                        is_active=True, join_date=datetime.now(), )
                    user_model.save()
                    return redirect('/customerlist/')
                elif duration_count.name == "Day":
                    user_model = Customer.objects.update(is_active=True, join_date=datetime.now(), expire_date=(
                        now+timedelta(days=int(duration_count.duration), hours=now.hour, minutes=now.minute, seconds=now.second)).isoformat())
                    user_model.save()
                    return redirect('/customerlist/')
            return redirect('/customerlist/')
    else:
        return redirect('/login/')


def customerDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(Customer, pk=id)
        data.delete()
        return redirect('/customerlist/')
    else:
        return redirect('/login/')


def customerEdit(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Customer, pk=id)
        instance.password = _pw()
        instance.save()

        return redirect('/customerlist/')

    else:
        return redirect('/login/')


def _pw(length=6):
    s = ''
    for i in range(length):
        s += choice(digits + ascii_letters)
    return s
