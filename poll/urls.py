from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index_view'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
