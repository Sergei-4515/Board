from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, ReplyCreate, Replies, CategoryList


urlpatterns = [
   path('', PostsList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/reply/', ReplyCreate.as_view(), name='reply_create'),

   path('my_replies/', Replies.as_view(), name='my_replies'),

   path('categories/<int:pk>/', CategoryList.as_view(), name='category_list'),

]