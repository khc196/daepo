from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ThingView, RequestView, ChatView, TackleView

thing_list = ThingView.as_view({
        'post': 'create',
        'get': 'list'
    })

thing_detail = ThingView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
request_list = RequestView.as_view({
        'post': 'create',
        'get': 'list'
    })

request_detail = RequestView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
chat_list = ChatView.as_view({
        'post': 'create',
        'get': 'list'
    })

chat_detail = ChatView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
tackle_list = TackleView.as_view({
        'post': 'create',
        'get': 'list'
    })

tackle_detail = TackleView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
urlpatterns = format_suffix_patterns([
        path('auth/', include('rest_framework.urls',
            namespace='rest_framework')),
        path('thing/', thing_list, name='thing_list'),
        path('thing/<int:pk>/', thing_detail, name='thing_detail'),
        path('request/', request_list, name='request_list'),
        path('request/<int:pk>/', chat_detail, name='request_detail'),
        path('chat/', chat_list, name='chat_list'),
        path('chat/<int:pk>/', chat_detail, name='chat_detail'),
        path('tackle/', tackle_list, name='tackle_list'),
        path('tackle/<int:pk>/', tackle_detail, name='tackle_detail'),
    ])
