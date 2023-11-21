from django.shortcuts import render
from django.urls import reverse_lazy
from clinicalsApp.models import Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname', 'lastName','age')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname', 'lastName','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname', 'lastName','age')
