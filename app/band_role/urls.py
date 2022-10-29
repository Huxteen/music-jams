
from django.urls import path
from band_role import views

urlpatterns = [
    path('', views.BandRoleList.as_view(), name="band-role-create-list"),
    path('<int:pk>/', views.BandRoleDetail.as_view(),
         name="band-role-detail"),
    path('list/', views.BandRoleUserListAPiView.as_view(),
         name="list-all-active-band-role"),
    path('user/', views.UserBandRoleCreateAPIView.as_view(),
         name="create-user-band-role"),
    path('user/list', views.UserBandRoleListAPIView.as_view(),
         name="list-user-band-role"),
]
