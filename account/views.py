from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class SignupView(FormView):
    form_class = forms.RegisterForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('strona:strona-home')
    def form_valid(self, form):
        user = form.save(commit = False)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

class LoginView(FormView):

    form_class = forms.LoginForm
    success_url = reverse_lazy('strona:strona-home')
    template_name = 'account/login.html'

    def form_valid(self, form):
        credentials = form.cleaned_data
        user = authenticate(username = credentials['email'],
                            password = credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:

            messages.add_message(self.request, messages.INFO, 'nieprawidłowe dane, spróbuj ponownie')

            return HttpResponseRedirect(reverse_lazy('account:login'))


def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('strona:strona-home'))
