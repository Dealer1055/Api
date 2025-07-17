from django.contrib import admin
from django.urls import path
from api.views import AuthorAPIView, GenreAPIView, BookAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse
from django.urls import path
from django.contrib import admin
from api.views import AuthorAPIView, GenreAPIView, BookAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Kutubxona API",
      default_version='v1',
      description="Author, Genre, Book API hujjatlari",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/authors/', AuthorAPIView.as_view()),
    path('api/authors/<int:pk>/', AuthorAPIView.as_view()),

    path('api/genres/', GenreAPIView.as_view()),
    path('api/genres/<int:pk>/', GenreAPIView.as_view()),

    path('api/books/', BookAPIView.as_view()),
    path('api/books/<int:pk>/', BookAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]