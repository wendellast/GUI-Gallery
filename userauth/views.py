from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from userauth.forms import UserRegisterForm

from django.views import View
from .forms import UserLoginForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm



class PageLogin(View):
    template_name = 'sign-in.html'
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("gui:index")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("gui:index")

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Você está logado")
                return redirect("gui:index")
            else:
                messages.warning(request, "Credenciais inválidas.")
        else:
            messages.warning(request, "Por favor, corrija os erros abaixo.")

        return render(request, self.template_name, {'form': form})

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'sign-up.html'
    success_url = reverse_lazy('gui:index')  # Redireciona para a URL com nome 'gui:index'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("gui:index")
