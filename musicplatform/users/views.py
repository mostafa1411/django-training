from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.

class RegisterUserView(View):
    template_name = 'users/register.html'
    registerForm = UserCreationForm()

    def get(self, request):
        context = {'form': self.registerForm}
        return render(request, self.template_name, context)

    def post(self, request):
        self.registerForm = UserCreationForm(request.POST)
        if self.registerForm.is_valid():
            self.registerForm.save()

        context = {'form': self.registerForm}
        return render(request, self.template_name, context)


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

# def registerUser(request):
#     registerForm = UserCreationForm()
#
#     if request.method == 'POST':
#         registerForm = UserCreationForm(request.POST)
#         if registerForm.is_valid():
#             registerForm.save()
#
#     context = {'form': registerForm}
#     return render(request, 'users/register.html', context)
#
#
# def loginUser(request):
#     loginForm = AuthenticationForm()
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#         else:
#             messages.info(request, 'Username or password is incorrect!')
#
#     context = {'form': loginForm}
#     return render(request, 'users/login.html', context)