from rest_framework import viewsets, permissions
from .models import Project, Environment, SecretVersion
from .serializers import ProjectSerializer, EnvironmentSerializer, SecretVersionSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset= Project.objects.all()

    def get_queryset(self):
        return self.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EnvironmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Environment.objects.all()

    def get_queryset(self):
        return self.objects.filter(project__owner=self.request.user)

class SecretVersionViewSet(viewsets.ModelViewSet):
    serializer_class = SecretVersionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SecretVersion.objects.all()

    def get_queryset(self):
        return self.objects.filter(environment__project__owner=self.request.user)

    def perform_create(self, serializer):
        # You may want to auto-increment the version
        last_version = SecretVersion.objects.filter(
            environment=serializer.validated_data['environment']
        ).order_by('-version').first()
        next_version = (last_version.version + 1) if last_version else 1
        serializer.save(created_by=self.request.user, version=next_version)
