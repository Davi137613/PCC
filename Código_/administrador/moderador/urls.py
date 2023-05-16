from os import path
from django import views


urlpatterns = [
    path('list/', views.moderador_list, name='moderador_list'),
    path('create/', views.moderador_create, name='moderador_create'),
    path('update/', views.moderador_update, name='moderador_update'),
    path('delete/', views.moderador_delete, name='moderador_delete'),


    # URL para o formulário de desativação de usuário
    path('users/<int:pk>/deactivate/', views.deactivate_user_view, name='deactivate_user'),

    # URL para o formulário de desativação de post
    path('posts/<int:pk>/deactivate/', views.deactivate_post_view, name='deactivate_post'),

    # URL para o formulário de desativação de comentário
    path('comments/<int:pk>/deactivate/', views.deactivate_comment_view, name='deactivate_comment'),
]



