from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    #func base view
    # path('email/', views.onEmail, name='email'),
    # path('viewemail/', views.onProcessView, name='view_email'),
    #class base view
    path('email/', views.OnEmail.as_view(), name='email'),
    path('viewemail/', views.OnProcessView.as_view(), name='view_email'),
]
