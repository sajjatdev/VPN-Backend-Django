
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Loginapp.models import User
from ..models import ServerJson, Customer


def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        updatecount = ServerJson.objects.all().count
        if userdata.is_admin is True:
            customerCount = Customer.objects.all().count
            sellers = User.objects.all().count
            return render(request, 'index.html', context={'User_data': userdata, 'updatecount': updatecount, 'sellers': sellers, 'customerCount': customerCount})
        else:
            customerCount = Customer.objects.filter(
                reseller=current_user.id).count
            sellers = User.objects.filter(createby=current_user.id).count
            return render(request, 'index.html', context={'User_data': userdata, 'updatecount': updatecount, 'sellers': sellers, 'customerCount': customerCount})
    else:
        return redirect('/login/')
