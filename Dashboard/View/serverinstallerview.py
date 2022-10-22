
from paramiko import SSHClient, AutoAddPolicy
from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from Loginapp.models import User
from ..forms import ServerInstaller as serverform


def ServerInstall(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            dataform = serverform(request.POST)
            if dataform.is_valid():
                try:
                    ssh = SSHClient()
                    ssh.set_missing_host_key_policy(AutoAddPolicy())
                    hostname = dataform.cleaned_data['server_host']
                    username = dataform.cleaned_data['username']
                    password = dataform.cleaned_data['password']
                    print("Form Data Get Done")
                    ssh.connect(hostname=hostname,
                                username=username, password=password)
                    print("Server Connect Done")

                    stdin, stdout, stderr = ssh.exec_command(
                        'wget -O openvpn.sh https://get.vpnsetup.net/ovpn;sudo bash openvpn.sh --auto')
                    print(stdout.read().decode())
                    print("Server Install  Done")
                    ssh.close()

                    dataform.save()
                    return redirect('/install/')
                except Exception as e:
                    return redirect('/install/')
            else:
                return redirect('/install/')
                print("Form Error")
        else:
            current_user = request.user
            userdata = get_object_or_404(
                User, pk=current_user.id)
            dataform = serverform()
            query_set=ServerInstaller.objects.all()
            return render(request, 'server_install/serverlist.html', context={'User_data': userdata, 'form': dataform,'server_data':list(query_set)})
    else:
        return redirect('/login/')


def serverReset(request,id):
    if request.user.is_authenticated:
            try:
                    server_data=ServerInstaller.objects.get(pk=id)
                    ssh = SSHClient()
                    ssh.set_missing_host_key_policy(AutoAddPolicy())
                    print("Form Data Get Done")
                    ssh.connect(hostname=server_data.server_host,
                                username=server_data.username, password=server_data.password)
                    print("Server Connect Done")

                    stdin, stdout, stderr = ssh.exec_command(
                        'sudo systemctl restart openvpn@server.service')
                    print(stdout.read().decode())
                    print("Server Reset  Done")
                    ssh.close()
                    return redirect('/install/')
            except Exception as e:
                    print(e)
                    return redirect('/install/')
    else:
        return redirect('/login/')        

    


def serverStart(request,id):
    if request.user.is_authenticated:
            try:
                    server_data=ServerInstaller.objects.get(pk=id)
                    ssh = SSHClient()
                    ssh.set_missing_host_key_policy(AutoAddPolicy())
                    print("Form Data Get Done")
                    ssh.connect(hostname=server_data.server_host,
                                username=server_data.username, password=server_data.password)
                    print("Server Connect Done")

                    stdin, stdout, stderr = ssh.exec_command(
                        'sudo systemctl start openvpn@server.service')
                    print(stdout.read().decode())
                    print("Server Start  Done")
                    ssh.close()
                    server_data.status=True
                    server_data.save()
                    return redirect('/install/')
            except Exception as e:
                    print(e)
                    return redirect('/install/')
    else:
        return redirect('/login/')         


def serverStop(request,id):
    if request.user.is_authenticated:
            try:
                    server_data=ServerInstaller.objects.get(pk=id)
                    ssh = SSHClient()
                    ssh.set_missing_host_key_policy(AutoAddPolicy())
                    print("Form Data Get Done")
                    ssh.connect(hostname=server_data.server_host,
                                username=server_data.username, password=server_data.password)
                    print("Server Connect Done")

                    stdin, stdout, stderr = ssh.exec_command(
                        'sudo systemctl stop openvpn@server.service')
                    print(stdout.read().decode())
                    print("Server Stop  Done")
                    ssh.close()
                    server_data.status=False
                    server_data.save()
                    return redirect('/install/')
            except Exception as e:
                    print(e)
                    return redirect('/install/')
    else:
        return redirect('/login/')         