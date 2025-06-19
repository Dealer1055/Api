from django.urls import path
from .views import home_page, AuthorApiView

urlpsatterns = [
    path('', home_page, name='home'),
    path('authors/', AuthorApiView.as_view()),
]