from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CodeForm
from pages.models import CustomUser
from .utils import send_sms
from django.shortcuts import redirect
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def home_view(request):
    return render(request, 'main.html', {})

def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('login') #remember to change after verify page is done
    return render(request, 'auth.html', {'form': form})        

def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk = pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            send_sms(code_user, user.phone_number)
            print(code_user)
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('home')
            else:
                return redirect('login-view')
    return render(request, 'verify.html', {'form' : form})
