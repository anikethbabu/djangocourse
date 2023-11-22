from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from clinicalsApp.models import Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

# Create your views here.
class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName','age')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName','age')

def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form, 'patient': patient})
