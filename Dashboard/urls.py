from django.urls import path
from .View.transaction import transaction_add, transaction_list
from .View.CustomerView import CustomerList, CustomerCreate, customerEdit, customerStatus, customerDelete
from .View.MembershipView import MambershipCreate, MembershipList, MembershipEdit, MembershipDelete
from .View.UpdateView import update_add, updateList, updateEdit, PayloadDelete, PayloadList, ServerDelete, ServerUpdate, updateDelete, ServerList, PayloadAdd, PayloadUpdate, ServerAdd
from .View.ResellerView import ResellerAdd, ResellerList, ResellerEdit, ResellerDelete, resellerStatus
from .View.views import index
app_name = "Home"
urlpatterns = [
    path('', index, name='home'),
    # Update Url Start
    path('updateadd/', update_add, name='update_add'),
    path('updatelist/', updateList, name="updatelist"),
    path('edit/<str:id>/', updateEdit, name="updateEdit"),
    path('delete/<str:id>/', updateDelete, name="updelete"),
    # ReSeller URl Start
    path('reselleradd/', ResellerAdd, name='reselleradd'),
    path('resellerlist/', ResellerList, name="resellerlist"),
    path('resellerEdit/<int:id>/', ResellerEdit, name="resellerEdit"),
    path('resellerdelete/<int:id>/', ResellerDelete, name="resellerdelete"),
    path('resellerStatus/<int:id>/', resellerStatus, name="resellerStatus"),
    # Membership URL Start
    path('membershipcreate/', MambershipCreate, name="MambershipCreate"),
    path('MembershipList/', MembershipList, name='MembershipList'),
    path('membershipEdit/<int:id>/', MembershipEdit, name="membershipEdit"),
    path('membershipdelete/<int:id>/', MembershipDelete, name="membershipdelete"),
    # Customer URL Start
    path('customercreate/', CustomerCreate, name="customercreate"),
    path('customerlist/', CustomerList, name='customerlist'),
    path('customerEdit/<int:id>/', customerEdit, name="customerEdit"),
    path('customerdelete/<int:id>/', customerDelete, name="customerdelete"),
    path('customerStatus/<int:id>/', customerStatus, name="customerStatus"),
    # Customer URL Start
    path('transactionadd/', transaction_add, name="transactionadd"),
    path('transactionlist/', transaction_list, name='transactionlist'),
    # Server URL Start
    path('serveradd/', ServerAdd, name='serveradd'),
    path('serverlist/', ServerList, name="serverlist"),
    path('serverupdate/<int:id>/', ServerUpdate, name='serverupdate'),
    path('serverdelete/<int:id>/', ServerDelete, name='serverdelete'),
    # Payload URl Start
    path('payloadadd/', PayloadAdd, name='payloadadd'),
    path('payloadlist/', PayloadList, name="payloadlist"),
    path('payloadupdate/<int:id>/', PayloadUpdate, name='payloadupdate'),
    path('payloaddelete/<int:id>/', PayloadDelete, name='payloaddelete'),

]
