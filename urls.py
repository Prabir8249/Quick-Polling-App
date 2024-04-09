from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('create/', views.create_poll, name='create_poll'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/result/', views.poll_result, name='poll_result'),
    path('<int:poll_id>/ajax_vote/', views.ajax_vote, name='ajax_vote'),
    path('ajax_create/', views.ajax_create_poll, name='ajax_create_poll'),
]
