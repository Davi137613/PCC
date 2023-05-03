from os import path
from django import views
from .views import AdminListView, AdminCreateView, AdminUpdateView, AdminDeleteView

app_name = 'administrador'

urlpatterns = [
path('', AdminListView.as_view(), name='administrador_list'),
path('create/', AdminCreateView.as_view(), name='administrador_create'),
path('<int:pk>/update/', AdminUpdateView.as_view(), name='administrador_update'),
path('<int:pk>/delete/', AdminDeleteView.as_view(), name='administrador_delete'),


# URL para o formulário de contato com o administrador
path('contact/', views.contact_admin_view, name='contact_admin'),

# URL para o formulário de desativação de usuário
path('users/<int:pk>/deactivate/', views.deactivate_user_view, name='deactivate_user'),

# URL para o formulário de desativação de post
path('posts/<int:pk>/deactivate/', views.deactivate_post_view, name='deactivate_post'),

# URL para o formulário de desativação de comentário
path('comments/<int:pk>/deactivate/', views.deactivate_comment_view, name='deactivate_comment'),
]




