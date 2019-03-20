from .models import *
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
def patient_list(request):
    patient = Patient.objects.filter(created_date__lte=timezone.now())
    return render(request, 'patients/patient_list.html',
                 {'patients': patient})

def patient_new(request):
   if request.method == "POST":
       form = PatientForm(request.POST)
       if form.is_valid():
           patient = form.save(commit=False)
           patient.created_date = timezone.now()
           patient.save()
           patients = Patient.objects.filter(created_date__lte=timezone.now())
           return render(request, 'patients/patient_list.html',
                         {'patients': patients})
   else:
       form = PatientForm()
       # print("Else")
   return render(request, 'patients/patient_new.html', {'form': form})

def patient_edit(request, pk):
   patient = get_object_or_404(Patient, pk=pk)
   if request.method == "POST":
       # update
       form = PatientForm(request.POST, instance=patient)
       if form.is_valid():
           patient = form.save(commit=False)
           patient.updated_date = timezone.now()
           patient.save()
           patient = Patient.objects.filter(created_date__lte=timezone.now())
           return render(request, 'patients/patient_list.html',
                         {'patients': patient})
   else:
        # edit
       form = PatientForm(instance=patient)
   return render(request, 'patients/patient_edit.html', {'form': form})

def patient_delete(request, pk):
   patient = get_object_or_404(Patient, pk=pk)
   patient.delete()
   return redirect('patients:patient_list')

#Injury Report
#Patient Triage







