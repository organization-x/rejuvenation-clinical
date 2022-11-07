from django.urls import path

from .views import SignInView
from .views import DashboardView
from .views import InformedConsentView
from .views import SingleTrialView



urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="Dashboard"),
    path("informedconsent/", InformedConsentView.as_view(), name="InformedConsent"),
    path("singletrial/", SingleTrialView.as_view(), name="SingleTrial"),
]