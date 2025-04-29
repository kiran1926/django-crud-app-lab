from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='plants-index'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
    path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
    path('plants/<int:plant_id>/add-fertilizer/', views.add_fertilizer, name='add-fertilizer'),
    path('accounts/signup/', views.signup, name='signup'),
]