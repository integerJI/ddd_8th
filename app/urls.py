from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('model', views.model, name="model"),
    # path('create/', views.CreateInvitationView.as_view(), name='create'),
    # path('detail/<str:invi_key>', views.detail, name='detail'),
]
