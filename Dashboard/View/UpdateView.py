from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Loginapp.models import User
from ..models import update
from ..forms import UpdateForm

def update_add(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        if request.method == 'POST':
            name = request.POST['updatename']
            jsondata = request.POST['jsondata']
            data = update.objects.create(
                name=name, jsondata=jsondata, status=True,)
            data.save()
            print("Data Save Success")
            return redirect('/updatelist/')
        else:
            return render(request, 'update/updateadd.html', context={'User_data': userdata})
    else:
        return redirect('/login/')


def updateList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        query_set = update.objects.all()
        return render(request, 'update/updatelist.html', context={'User_data': userdata, 'update_data': list(query_set)})
    else:
        return redirect('/login/')


def updateEdit(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(update, pk=id)
        current_user = request.user
        userdata = get_object_or_404(User, pk=current_user.id)
        form = UpdateForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            print("Data Update Success")
            return redirect('/updatelist/')
        return render(request, 'update/editupdate.html', context={'editform': form, 'User_data': userdata, })

    else:
        return redirect('/login/')


def updateDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(update, pk=id)
        data.delete()
        return redirect('/updatelist/')
    else:
        return redirect('/login/')
