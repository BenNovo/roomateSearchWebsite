from django.conf.urls import urls

from . import consumers

websocket_urlpatterns = [
	url(r'^ws/chatroom/(?P<room_name>[^/]+)/$', Consumers.chatroomConsumer),
]