from app import views
from app.views import home, HospitalDetailView
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital_detail'),
    path('logout/',auth_views.LogoutView.as_view(next_page='homepage'),name='logout'),
    path('addresources',views.AddResource,name='addresources'),
    path('tracker',views.Tracker,name='tracker'),
]
