from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, FormView, RedirectView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator

User = get_user_model()


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/index.html", {})


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/login.html", {})


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/register.html", {})


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/form.html", {})


