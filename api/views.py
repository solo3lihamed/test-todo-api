from rest_framework import viewsets, generics, permissions
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from django.contrib.auth.models import User

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.todos.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]