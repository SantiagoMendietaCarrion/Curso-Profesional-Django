from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name='resume_foundation'),
    path('home1/', views.Home1View.as_view(), name='home1'),
]