from django.urls import path,include
from dashboard import views
app_name = "dashboard"
urlpatterns = [
    path('', views.home, name="home"),
    path('scholarship/', views.scholarship, name="scholarship"),
    path('scholarship_view/<id>/', views.scholarship_view, name="scholarship_view"),
    path('scholarship_edit/<id>/', views.scholarship_edit, name="scholarship_edit"),
]
