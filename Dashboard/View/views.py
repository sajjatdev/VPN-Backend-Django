
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Loginapp.models import User
from ..models import update
from ..forms import UpdateForm


def index(request):
    if request.user.is_authenticated:
        current_user = request.user

        userdata = get_object_or_404(User, pk=current_user.id)
        updatecount = update.objects.all().count
        sellers = User.objects.filter(createby=current_user.id).count
        return render(request, 'index.html', context={'User_data': userdata, 'updatecount': updatecount, 'sellers': sellers})
    else:
        return redirect('/login/')
