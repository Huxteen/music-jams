
from django.urls import path
from jams import views

urlpatterns = [
    path('', views.JamList.as_view(), name="users-jam-list"),
    path('create/', views.CreateJamAPIView.as_view(), name="user-create-jam"),
    path('<int:pk>/', views.JamDetail.as_view(), name="user-jam-detail"),
    path('list/', views.JamListAPiView.as_view(), name="list-all-jam"),
    path('band-role/', views.JamBandRoleList.as_view(),
         name="list-jam-band-role"),
    path('band-role/<int:pk>/', views.JamBandRoleDetail.as_view(),
         name="jam-band-role-detail"),
    path('start/<int:pk>/', views.StartJamDetail.as_view(),
         name="user-start-jam"),
    path('join/', views.JamInvitationList.as_view(), name="user-join-jam"),
    path('join/<int:pk>/', views.JamInvitationDetail.as_view(),
         name="user-join-detail"),
]
