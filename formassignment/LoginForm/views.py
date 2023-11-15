from django.shortcuts import render
from . import forms
# Create your views here.

def LoginForm(request):
    form = forms.LoginForm()
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("User Name", form.cleaned_data['userName'])
            print("Password", form.cleaned_data['password'])

    return render(request,'login.html', {'form': form})
