from django.urls import path
from .views import PostDelete, PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail')
    path('<int:pk>/', PostUpdate.as_view(), name='post_update')
    path('<int:pk>/', PostDelete.as_view(), name='post_delete')
]