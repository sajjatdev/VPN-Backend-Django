from django.urls import path
from .View.MembershipView import MambershipCreate, MembershipList, MembershipEdit, MembershipDelete
from .View.UpdateView import update_add, updateList, updateEdit, updateDelete
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
]
