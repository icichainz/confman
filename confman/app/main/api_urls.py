from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, EnvironmentViewSet, SecretVersionViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'secrets', SecretVersionViewSet)

urlpatterns = router.urls
