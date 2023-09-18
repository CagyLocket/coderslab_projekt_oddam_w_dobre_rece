from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, FormView, RedirectView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Donation, Institution
from .forms import NewUserForm

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


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'charity/login.html'

    def get_success_url(self):
        return reverse_lazy('charity:landing-page')

    def form_invalid(self, form):
        messages.error(self.request, 'Wprowadź poprawne dane w polach „adres e-mail” i „hasło” dla konta należącego do zespołu. Uwaga: wielkość liter może mieć znaczenie.')
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    url = reverse_lazy("charity:landing-page")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class Register(CreateView):
    model = User
    template_name = 'charity/register.html'
    form_class = NewUserForm

    def get_success_url(self):
        return reverse_lazy('charity:login')

    def form_invalid(self, form):
        messages.error(self.request, 'Wypełnij poprawnie wszystkie pola w formularzu.')
        return self.render_to_response(self.get_context_data(form=form,))


class ResetPassword(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/reset-password.html", {})


class AddDonation(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        return render(request, "charity/form.html", {})


class UserProfile(View):
    def get(self, request, *args, **kwargs):
        return render(request, "charity/user_profile.html", {})