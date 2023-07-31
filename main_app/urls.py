from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations_index, name='index'),
    path('destinations/<int:destination_id>/', views.destinations_detail, name='detail'),
    path('destinations/create/', views.DestinationCreate.as_view(), name='destinations_create'),
    path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destinations_update'),
    path('destinations/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destinations_delete'),
    path('destinations/<int:destination_id>/add_weather/', views.add_weather, name='add_weather'),
    path('destinations/<int:destination_id>/assoc_activity/<int:activity_id>/', views.assoc_activity, name='assoc_activity'),
    path('destinations/<int:destination_id>/unassoc_activity/<int:activity_id>/', views.unassoc_activity, name='unassoc_activity'),
    path('activities/', views.ActivityList.as_view(), name='activities_index'),
    path('activities/<int:pk>/', views.ActivityDetail.as_view(), name='activities_detail'),
    path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),

 ]