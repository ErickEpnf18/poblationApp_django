from django.urls import path
from .views import cities, delete_province


urlpatterns = [
    path('', cities),
    path('delete_province/<int:data_id>/', delete_province, name='delete_province')
]