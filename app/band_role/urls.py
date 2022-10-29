
from django.urls import path
from band_role import views

urlpatterns = [
    path('', views.BandRoleList.as_view(), name="band-role-list"),
    path('<int:pk>/', views.BandRoleDetail.as_view()),
    path('list/', views.BandRoleUserListAPiView.as_view()),
    path('user/', views.UserBandRoleList.as_view()),
]
