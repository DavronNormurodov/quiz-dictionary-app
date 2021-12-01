from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from .models import User
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    return render(request, "index.html")


# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = "accounts/register.html"
#     success_url = "/"
#     def form_valid(self, form):
#         request = self.request
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         return redirect('register')

def RegisterView(request):
    form = RegisterForm(request.POST or None)
    contex = {"form": form}
    if form.is_valid():
        form.save()
        # username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        # User.objects.create_user(username, email, password)
    else:
        form = RegisterForm()
        contex = {"form": form}
    return render(request, "accounts/register.html", contex)


class LoginView(FormView):
    form_class = LoginForm  
    success_url = '/'
    template_name = "accounts/login.html"

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            
        return super(LoginView, self).form_invalid(form)


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     contex = {"form": form}
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
    
#     return render(request, "accounts/login.html", contex)

class LogoutView(TemplateView):
    # success_url = '/'
    template_name = "index.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)