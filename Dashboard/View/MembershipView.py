from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..models import Membership
from ..forms import MembershipForm
# Membership Create Block Start


def MambershipCreate(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        formdata = MembershipForm()
        if request.method is "POST":
            pass
        else:
            return render(request, 'Membership/Membershipadd.html', context={'User_data': userdata, 'forms': formdata})

    else:
        return redirect('/login/')
