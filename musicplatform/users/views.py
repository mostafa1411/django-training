from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.


class LoginUserView(View):
    template_name = 'users/login.html'
    loginForm = AuthenticationForm()

    def get(self, request):
        context = {'form': self.loginForm}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.info(request, 'Username or password is incorrect!')

        context = {'form': self.loginForm}
        return render(request, self.template_name, context)


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
