from django.urls import path
from .views import UpdateClientView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('clients/update/kamuikatsuragi/chronoshindou/adhkmvs262452156625981016101412/<int:pk>', login_required(function=UpdateClientView.as_view(), login_url='login') , name='updateclient'),
]
