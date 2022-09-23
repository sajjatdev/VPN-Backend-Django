from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..models import Membership
from ..forms import MembershipForm
# Membership Create Block Start


def MambershipCreate(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        if request.method == "POST":
            form = MembershipForm(request.POST)
            if form.is_valid():
                print("Welcome")
                form.save()
                return redirect('/MembershipList/')
        else:
            formdata = MembershipForm()
            return render(request, 'Membership/Membershipadd.html', context={'User_data': userdata, 'forms': formdata})

    else:
        return redirect('/login/')


def MembershipList(request):
    if request.user.is_authenticated:
        query_set = Membership.objects.all()
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        return render(request, 'Membership/MembershipList.html', context={'User_data': userdata, 'membershipList': list(query_set)})
    else:
        return redirect('/login/')


def MembershipEdit(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Membership, pk=id)
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        form = MembershipForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            print("Data Update Success")
            return redirect('/MembershipList/')
        return render(request, 'Membership/MembershipUpdate.html', context={'editform': form, 'User_data': userdata, })

    else:
        return redirect('/login/')


def MembershipDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(Membership, pk=id)
        data.delete()
        return redirect('/MembershipList/')
    else:
        return redirect('/login/')
