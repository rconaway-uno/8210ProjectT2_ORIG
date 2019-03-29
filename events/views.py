
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'events/home.html',
                  {'events': home})

def adminlogin(request):

    if request.user.is_staff:
        return redirect('events/nurse_home.html')
    else:
        return redirect('events/admin_home.html')

@permission_required('is_superuser')
def admin_home(request):
    return render(request, 'events/admin_home.html',
                  {'admin': admin_home})

@permission_required('is_staff')
def admin_home(request):

    return render(request, 'events/admin_home.html',
                  {'chs': admin_home})

def admin_login(request):
        return render(request, 'events/admin_login.html', {'events': admin_login})

@login_required
def nurse_home(request):
    return render(request, 'events/nurse_home.html',
                  {'nurse': nurse_home})




@login_required
def users_list(request):
    users = User.objects.all()
    #print(users)
    return render(request, 'events/users_list.html', {'users': users})



@login_required
def user_option(request):
    return render(request, 'events/user_option.html',
                 {'admin': user_option})

@login_required
def nurse_list(request):
    users = User.objects.filter(groups=2)
    return render(request, 'events/nurse_list.html',{'users': users})

@login_required
def user_edit(request, pk):
   user = get_object_or_404(User, pk=pk)
   if request.method == "POST":
       # update
       form = UserEditForm(request.POST, instance=user)
       if form.is_valid():
           user = form.save(commit=False)
           user.updated_date = timezone.now()
           user.save()
           users = User.objects.filter()
           print(users)
           return render(request, 'events/users_list.html',
                         {'users': users})
   else:
        # edit
       form = UserEditForm(instance=user)
       return render(request, 'events/user_edit.html', {'form': form})

@login_required
def user_delete(request, username):
    users = User.objects.get(username=username)
    users.delete()
    return redirect('events:users_list')


@login_required
def user_new(request):
   if request.method == "POST":
       form = UserEditForm(request.POST)
       if form.is_valid():
           newuser = form.save(commit=False)
           newuser.date_joined = timezone.now()
           newuser.save()
           users = User.objects.filter(date_joined__lte=timezone.now())
           return render(request, 'events/users_list.html',
                         {'users': users})
   else:
       form = UserEditForm()
       # print("Else")
   return render(request, 'events/user_new.html', {'form': form})




def event_list(request):
    event = Event.objects.filter(created_date__lte=timezone.now())
    return render(request, 'events/event_list.html',
                 {'events': event})

def event_new(request):
   if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           event = form.save(commit=False)
           event.created_date = timezone.now()
           event.save()
           events = Event.objects.filter(created_date__lte=timezone.now())
           return render(request, 'events/event_list.html',
                         {'events': events})
   else:
       form = EventForm()
       # print("Else")
   return render(request, 'events/event_new.html', {'form': form})


def event_edit(request, pk):
   event = get_object_or_404(Event, pk=pk)
   if request.method == "POST":
       # update
       form = EventForm(request.POST, instance=event)
       if form.is_valid():
           event = form.save(commit=False)
           event.updated_date = timezone.now()
           event.save()
           event = Event.objects.filter(created_date__lte=timezone.now())
           return render(request, 'events/event_list.html',
                         {'events': event})
   else:
        # edit
       form = EventForm(instance=event)
   return render(request, 'events/event_edit.html', {'form': form})

def event_delete(request, pk):
   event = get_object_or_404(Event, pk=pk)
   event.delete()
   return redirect('events:event_list')
