from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
   'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
   'get': 'list'
})
user_detail = UserViewSet.as_view({
   'get': 'retrieve'
})

urlpatterns = [
   path('snippets/', snippet_list, name='snippet-list'),
   path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
   path('users/', user_list, name='user-list'),
   path('users/<int:pk>/', user_detail, name='user-detail'),
   path('auth/', include('rest_framework.urls')),
   path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
   path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)