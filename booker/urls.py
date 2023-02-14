from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='room_detail'),
    path('like/<slug:slug>', views.RoomLike.as_view(), name='room_like'),
    path('upload/<slug:slug>', views.UploadPage.as_view(), name='upload.html'),
]
