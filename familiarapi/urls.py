from django.urls import path
from .views import Index, FamiliarIdView, createFamiliar, deleteFamiliar, editFamiliar

urlpatterns = [
    path('', Index),
    path('<int:id>/', FamiliarIdView),
    path('edit/', editFamiliar),
    path('delete/<int:id>', deleteFamiliar),
    path('create/', createFamiliar),
]
