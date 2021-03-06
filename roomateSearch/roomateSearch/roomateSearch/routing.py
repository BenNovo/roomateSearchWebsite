from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatroom.routing

applicaion = ProtocolTypeRouter ({
	'websocket': AuthMiddlewareStack(
		URLRouter(
			chatroom.routing.websocket_urlpatterns
		)
	),
})