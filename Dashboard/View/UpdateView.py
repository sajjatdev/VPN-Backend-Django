
from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..models import ServerJson, Server, Payload
from ..forms import ServerJsonForm, ServerForm, PayloadForm


def update_add(request):
    if request.user.is_authenticated:

        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        if request.method == 'POST':
            form = ServerJsonForm(request.POST)
            if form.is_valid():
                form.save()
                print("Data Save Success")
                return redirect('/updatelist/')
            else:
                return redirect('/updatelist/')
        else:
            form = ServerJsonForm()
            return render(request, 'update/updateadd.html', context={'User_data': userdata, 'form': form})
    else:
        return redirect('/login/')


def updateList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        query_set = ServerJson.objects.all()
        return render(request, 'update/updatelist.html', context={'User_data': userdata, 'update_data': list(query_set)})
    else:
        return redirect('/login/')


def updateEdit(request, id):
    if request.user.is_authenticated:
        instance = get_object_or_404(ServerJson, pk=id)
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        form = ServerJsonForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            print("Data Update Success")
            return redirect('/updatelist/')
        return render(request, 'update/editupdate.html', context={'editform': form, 'User_data': userdata, })

    else:
        return redirect('/login/')


def updateDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(ServerJson, pk=id)
        data.delete()
        return redirect('/updatelist/')
    else:
        return redirect('/login/')


def ServerAdd(request):
    if request.user.is_authenticated:
        current_user = request.user

        userdata = get_object_or_404(
            User, pk=current_user.id)
        if request.method == "POST":
            forms = ServerForm(request.POST, request.FILES)
            print(forms.errors)
            if forms.is_valid():
                forms.save()
                print("success")
                return redirect('/serverlist/')
            else:
                return redirect('/serveradd/')
        else:
            form = ServerForm()
            return render(request, 'update/server/serveradd.html', context={'form': form, 'User_data': userdata, })
    else:
        return redirect('/login/')


def ServerList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        query_set = Server.objects.all()
        return render(request, 'update/server/serverlist.html', context={'User_data': userdata, 'server_data': list(query_set)})
    else:
        return redirect('/login/')


def ServerUpdate(request, id):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        server_data = Server.objects.get(id=id)
        if request.method == 'POST':
            formdata = ServerForm(
                request.POST, request.FILES, instance=server_data)
            if formdata.is_valid():
                formdata.save()
                return redirect('/serverlist/')
        else:
            form = ServerForm(instance=server_data)
            return render(request, 'update/server/serveredit.html', context={'User_data': userdata, 'form': form})
    else:
        return redirect('/login/')


def ServerDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(Server, pk=id)
        data.delete()
        return redirect('/serverlist/')
    else:
        return redirect('/login/')


def PayloadAdd(request):
    if request.user.is_authenticated:
        current_user = request.user

        userdata = get_object_or_404(
            User, pk=current_user.id)
        if request.method == "POST":
            forms = PayloadForm(request.POST)
            print(forms.errors)
            if forms.is_valid():
                forms.save()
                print("success")
                return redirect('/payloadlist/')
            else:
                return redirect('/payloadadd/')
        else:
            form = PayloadForm()
            return render(request, 'update/payload/payloadadd.html', context={'form': form, 'User_data': userdata, })
    else:
        return redirect('/login/')


def PayloadUpdate(request, id):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        server_data = Payload.objects.get(id=id)
        if request.method == 'POST':
            formdata = PayloadForm(
                request.POST, request.FILES, instance=server_data)
            if formdata.is_valid():
                formdata.save()
                return redirect('/payloadlist/')
        else:
            form = PayloadForm(instance=server_data)
            return render(request, 'update/payload/payloadedit.html', context={'User_data': userdata, 'form': form})
    else:
        return redirect('/login/')


def PayloadList(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        query_set = Payload.objects.all()
        return render(request, 'update/payload/payloadlist.html', context={'User_data': userdata, 'payload_data': list(query_set)})
    else:
        return redirect('/login/')


def PayloadDelete(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(Payload, pk=id)
        data.delete()
        return redirect('/payloadlist/')
    else:
        return redirect('/login/')
