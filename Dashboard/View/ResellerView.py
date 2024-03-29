
from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..forms import ReSellerForm
from ..models import Customer


def ResellerAdd(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        if request.method == "POST":

            username = request.POST['username']
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            credit = request.POST.get('credit', 0)
            is_admin = request.POST.get('admin_status', False)
            createby = current_user.id

            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if int(credit) <= userdata.credit or userdata.is_admin:
                        data = User.objects.create_user(
                            username=username,
                            credit=credit,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            createby=createby,
                            is_admin=is_admin,
                            passcode=password
                        )
                        data.save()
                        if not userdata.is_admin:
                            userdata.credit = int(userdata.credit)-int(credit)
                            userdata.save()
                        print("ReSeller Create success")
                        return redirect('/resellerlist/')
                    else:
                        form_post = ReSellerForm()
                        return render(request, 'reseller/reselleradd.html', context={'User_data': userdata, 'reseller_form': form_post, 'error': 'credit'})
                else:
                    form_post = ReSellerForm()
                    return render(request, 'reseller/reselleradd.html', context={'User_data': userdata, 'reseller_form': form_post, 'error': 'email'})
            else:
                form_post = ReSellerForm()
                return render(request, 'reseller/reselleradd.html', context={'User_data': userdata, 'reseller_form': form_post, 'error': 'username'})
        else:
            form_post = ReSellerForm()
            return render(request, 'reseller/reselleradd.html', context={'User_data': userdata, 'reseller_form': form_post, 'error': ''})
    else:
        return redirect('/login/')


def ResellerList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        if current_user.is_admin == True:
            resellerList = User.objects.all()
            return render(request, 'reseller/resellerList.html', context={'User_data': userdata, 'resellerList': resellerList})
        else:
            resellerList = User.objects.filter(
                createby=current_user.id).all()
            return render(request, 'reseller/resellerList.html', context={'User_data': userdata, 'resellerList': resellerList})

    else:
        return redirect('/login/')


def ResellerEdit(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(User, pk=id)
        password = User.objects.make_random_password(
            length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        instance.set_password(password)
        instance.passcode = password
        print(password)
        instance.save()
        print("Data Update Success")
        return redirect('/resellerlist/')

    else:
        return redirect('/login/')


def ResellerDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(User, pk=id)
        data.delete()
        return redirect('/resellerlist/')
    else:
        return redirect('/login/')


def resellerStatus(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            status = request.POST['status']
            data = get_object_or_404(User, pk=id)
            if status == "1":
                data.is_active = False

                data.save()
                try:
                    customer_data = Customer.objects.filter(reseller=id).all()
                    if not customer_data is None:
                        for cu_item in customer_data:
                            cu_item.is_active = False
                            cu_item.save()
                except Exception as e:
                    print(e)

            else:
                data.is_active = True
                print("2")
                data.save()
                try:
                    customer_data = Customer.objects.filter(reseller=id).all()
                    if not customer_data is None:
                        for cu_item in customer_data:
                            cu_item.is_active = True
                            cu_item.save()
                except Exception as e:
                    print(e)
            return redirect('/resellerlist/')
    else:
        return redirect('/login/')
