from django.contrib import admin
from django.urls import path, include
from def_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from core.views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")

projects_router = NestedDefaultRouter(router, r"projects", lookup="project")
projects_router.register(r"tasks", TaskViewSet, basename="project-tasks")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include("accounts.urls")),

    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),


    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
]
