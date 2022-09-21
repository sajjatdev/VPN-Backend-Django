import operator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..forms import ReSellerForm


def ResellerView(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        if request.method == "POST":

            username = request.POST['username']
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            credit = request.POST.get('credit', 0)
            is_admin = request.POST.get('admin_status', False)
            createby = current_user.id
            status = True

            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    data = User.objects.create_user(
                        username=username,
                        credit=credit,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        createby=createby,
                        status=status,
                        is_admin=is_admin,
                        passcode=password
                    )
                    data.save()
                    print("ReSeller Create success")
                    return redirect('/resellerlist/')
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
        userdata = get_object_or_404(User, pk=current_user.id)
        if current_user.is_admin == True:
            resellerList = User.objects.all()
            return render(request, 'reseller/resellerList.html', context={'User_data': userdata, 'resellerList': resellerList})
        else:
            resellerList = User.objects.filter(createby=current_user.id).all()
            return render(request, 'reseller/resellerList.html', context={'User_data': userdata, 'resellerList': resellerList})

    else:
        return redirect('/login/')
