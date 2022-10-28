
from django.urls import path
from jams import views

urlpatterns = [
    path('', views.JamList.as_view()),
    path('create/', views.CreateJamAPIView.as_view()),
    path('<int:pk>/', views.JamDetail.as_view()),
    path('list/', views.JamListAPiView.as_view()),
    path('band-role/', views.JamBandRoleList.as_view()),
    path('band-role/<int:pk>/', views.JamBandRoleDetail.as_view()),
    path('start/<int:pk>/', views.StartJamDetail.as_view()),
    path('join/', views.JamInvitationList.as_view()),
    path('join/<int:pk>/', views.JamInvitationDetail.as_view()),
]
