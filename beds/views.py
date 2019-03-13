

from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def home(request):
    return render(request, 'beds/home.html',
                  {'beds': home})

def adminlogin(request):

    if request.user.is_staff:
        return redirect('beds/nurse_home.html')
    else:
        return redirect('beds/admin_home.html')

@permission_required('is_superuser')
def admin_home(request):
    return render(request, 'beds/admin_home.html',
                  {'admin': admin_home})

@permission_required('is_staff')
def admin_home(request):

    return render(request, 'beds/admin_home.html',
                  {'chs': admin_home})

def admin_login(request):
        return render(request, 'beds/admin_login.html', {'beds': admin_login})

@login_required
def nurse_home(request):
    return render(request, 'beds/nurse_home.html',
                  {'nurse': nurse_home})





