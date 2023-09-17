from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, FormView, RedirectView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Donation, Institution

User = get_user_model()


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        donated_bags = Donation.objects.aggregate(total_bags=Sum('quantity'))['total_bags']
        supported_organizations = Institution.objects.count()
        foundations = Institution.objects.filter(type__contains='fundacja')
        organisations = Institution.objects.filter(type__contains='organizacja')
        fundraisers = Institution.objects.filter(type__contains='zbiorka')

        context = {
            'donated_bags': donated_bags,
            'supported_organizations': supported_organizations,
            'foundations': foundations,
            'organisations': organisations,
            'fundraisers': fundraisers,
        }
        return render(request, "charity/index.html", context)


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/login.html", {})


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/register.html", {})


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/form.html", {})


