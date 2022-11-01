from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home_screen_view(request, *args, **kwargs):
    context = {}
    return render(request, "pages/home.html", context)

class SignInView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "registration/login.html"

class DashboardView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "pages/dashboard.html"

class InformedConsentView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "pages/informed_consent.html"

class SingleTrialView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "pages/single_trial.html"
