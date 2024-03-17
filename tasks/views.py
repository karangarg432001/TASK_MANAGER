from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.pagination import PageNumberPagination
from .permissions import AdminPermission, RegularUserPermission

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': str(user.id)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': str(user.id)
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class TaskListCreate(generics.ListCreateAPIView):
    """
    List all tasks or create a new task.
    """
    queryset = Task.objects.order_by('-created_at')
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        completed = self.request.query_params.get('completed')
        if completed:
            queryset = queryset.filter(completed=completed)
        return queryset
    
    def get_permissions(self):
        if self.request.user.is_staff:
            permission_classes = [AdminPermission]
        else:
            permission_classes = [RegularUserPermission]
        return [permission() for permission in permission_classes]

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    List task by task id or update a task or partial update a task or delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.user.is_staff:
            permission_classes = [AdminPermission]
        else:
            permission_classes = [RegularUserPermission]
        return [permission() for permission in permission_classes]

