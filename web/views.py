from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form1 import UserForm
from django.shortcuts import render

# Create your views here.


class UserFormView(View):
    form_class = UserForm
    template_name = 'web/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'web/registration-form.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username='username', password='password')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('make:log')

        return render(request, 'web/registration-form.html', {'form': form})

# Create your views here.
