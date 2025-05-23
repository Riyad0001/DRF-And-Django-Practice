from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import View
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method=="POST":
        form=UserCreationForm
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect('notes:index')
    context={form:"form"}
    return render(request,"register.html",context)

class NewUserCreation(CreateView):
    form_class=UserCreationForm
    template_name="register.html"
    success_url=reverse_lazy('accounts:login')


