from django.urls import path
from . import views

urlpatterns = [
    path('bulletins/', views.list_all_bulletins, name='list_all_bulletins'),
    path('bulletins/create/', views.create_bulletin, name='create_bulletin'),
    path('bulletins/<int:bulletin_id>/', views.get_bulletin, name='get_bulletin'),
]
