from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
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

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('charity:landing-page')

        return render(request, "charity/login.html", {'error_message': 'Wprowadź poprawne dane w polach „adres e-mail” i „hasło” dla konta należącego do zespołu. Uwaga: wielkość liter może mieć znaczenie.'})


class LogoutView(RedirectView):
    url = reverse_lazy("charity:landing-page")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/register.html", {})

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            password = password1

        if User.objects.filter(email=email).exists():
            return redirect('charity:register')

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, username=email)
        if user is not None:
            return redirect('charity:login')

        return render(request, "charity/register.html")


class ResetPassword(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/reset-password.html", {})


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/form.html", {})


class UserProfile(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/user_profile.html", {})