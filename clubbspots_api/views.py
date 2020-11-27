from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User as AdminUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse, JsonResponse

def login_view(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('updateclient')

    else:
      form = AuthenticationForm()
    return render(request,'loginpage.html', {'form':form}) 

def logout_view(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('login')
