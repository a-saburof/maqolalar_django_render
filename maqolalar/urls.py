from django.urls import path 
from .views import MaqolaListView,MaqolaDetailView

urlpatterns = [
    path('',MaqolaListView.as_view(),name='home'),
    path('post/<int:pk>',MaqolaDetailView.as_view(),name='maqola_detail')
]