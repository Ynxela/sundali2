from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('', views.snippet_root),
    path('machines/', views.get_all_machines),
    path('tasks/', views.get_all_tasks),
]
