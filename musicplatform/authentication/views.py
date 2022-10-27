from django.contrib import messages
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegistrationSerializer

# Create your views here.


class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
                    "token": AuthToken.objects.create(user)[1],
                    "user": UserSerializer(user, context=self.get_serializer_context()).data
                }, status=status.HTTP_201_CREATED)


# class LoginUserView(View):
#     template_name = 'users/login.html'
#     loginForm = AuthenticationForm()
#
#     def get(self, request):
#         context = {'form': self.loginForm}
#         return render(request, self.template_name, context)
#
#     def post(self, request):
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
#         context = {'form': self.loginForm}
#         return render(request, self.template_name, context)
#
#
# class LogoutUserView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')
