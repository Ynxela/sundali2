from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.snippet_root),
    path('machines/', views.get_all_machines),
    path('tasks/', views.get_all_tasks),
    path('getMachinesLocation/', views.ViewMachineLocations)
]
