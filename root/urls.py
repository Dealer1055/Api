from django.http import JsonResponse
from django.urls import path
from django.contrib import admin
from api.views import AuthorAPIView, GenreAPIView, BookAPIView

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/authors/', AuthorAPIView.as_view()),
    path('api/authors/<int:pk>/', AuthorAPIView.as_view()),
    path('api/genres/', GenreAPIView.as_view()),
    path('api/genres/<int:pk>/', GenreAPIView.as_view()),
    path('api/books/', BookAPIView.as_view()),
    path('api/books/<int:pk>/', BookAPIView.as_view()),
]
