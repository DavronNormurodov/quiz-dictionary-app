from django.urls import path, include
from django.conf.urls import url
from .views import dictionary_view, dictionary_update_view, dictionary_delete_view, dictionary_search_view
app_name = 'dictionary'

urlpatterns = [
    path('', dictionary_view, name='dictionary-list'),
    path('update/<int:id>/', dictionary_update_view, name='dictionary-update'),
    path('delete/<int:id>/', dictionary_delete_view, name='dictionary-delete'),
    path('search/', dictionary_search_view, name='dict-search'),
]