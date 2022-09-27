from django.shortcuts import render, redirect, get_object_or_404
from Loginapp.models import User
from ..models import Transaction


def transaction_add(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        if request.method == "POST":
            username = request.POST['username']
            balance = request.POST['balance']
            try:
                user_data = User.objects.get(username=username)
                print(user_data.username)
                if not user_data is None:
                    if userdata.is_admin is False and userdata.credit > 0:
                        user_data.credit += int(balance)
                        userdata.credit -= int(balance)
                        user_data.save()
                        userdata.save()
                        data = Transaction.objects.create(
                            users_id=user_data.id, balance=int(balance), authors_id=current_user.id)
                        data.save()
                        return redirect('/transactionlist/')

                    elif userdata.is_admin is True:
                        user_data.credit += int(balance)
                        user_data.save()
                        data = Transaction.objects.create(
                            users_id=user_data.id,
                            balance=int(balance),
                            authors_id=current_user.id)
                        data.save()
                        return redirect('/transactionlist/')
                    else:
                        return render(request, 'transaction/transaction_add.html', context={'User_data': userdata, 'error': 'balance'})
                else:
                    return render(request, 'transaction/transaction_add.html', context={'User_data': userdata, 'error': 'username'})
            except Exception as a:
                print(a)
                return render(request, 'transaction/transaction_add.html', context={'User_data': userdata, 'error': 'username'})

        else:
            return render(request, 'transaction/transaction_add.html', context={'User_data': userdata, 'error': ''})
    else:
        return redirect('/login/')


def transaction_list(request):
    if request.user.is_authenticated:
        current_user = request.user
        userdata = get_object_or_404(
            User, pk=current_user.id)
        if current_user.is_admin == True:
            transactionList = Transaction.objects.all()
            return render(request, 'transaction/transaction.html', context={'User_data': userdata, 'transaction': transactionList})
        else:
            transactionList = Transaction.objects.filter(
                authors=current_user.id).all()
            return render(request, 'transaction/transaction.html', context={'User_data': userdata, 'transaction': transactionList})

    else:
        return redirect('/login/')
