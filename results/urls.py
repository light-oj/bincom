from django.urls import path
from . import views

app_name = 'results'
urlpatterns = [
    # results views
    path('', views.polling_unit_result_list, name='polling_unit_result_list'),
    path('create/', views.polling_create, name='poll-create'),
    path('poll/<uniqueid>/update/', views.polling_update, name='poll-update'),
    path('poll/<uniqueid>/delete/', views.polling_delete, name='poll-delete'),
    path('<result_id>/',views.polling_unit_result_detail, name='polling_unit_result_detail'),
]