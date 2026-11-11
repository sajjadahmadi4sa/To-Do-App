from rest_framework import viewsets
from tasks.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import DefaultPagination




class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['title']
    pagination_class = DefaultPagination
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)