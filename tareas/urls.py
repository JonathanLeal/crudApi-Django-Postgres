from django.urls import path
from .views import TareaView

urlpatterns = [
    path('', TareaView.as_view(), name='tareas_lista'),
    path('tareas/<int:id>', TareaView.as_view(), name='tareas_procesos')
]