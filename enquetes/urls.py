from django.urls import path
from enquetes.views import index

urlpatterns = [
    path('', index, name='index_enquete')
]