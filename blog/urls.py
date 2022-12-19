from django.urls import path
from . import views

urlpatterns = [
    path('delete_comment/<int:pk>/',views.delete_comment),
    path('update_comment/<int:pk>/',views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/',views.PostUpdate.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('tag/<str:slug>/',views.tag_page),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('category/<str:slug>/',views.category_page),
    path('<int:pk>/new_comment/',views.new_comment),
    # https://project-ztsct.run.goorm.io/blog/category/programming
    # programming만 떼어 views.py의 category_page()
    path('',views.PostList.as_view()),
    
]