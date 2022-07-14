from django.urls import re_path
from main.consumers import Consumer

ws_urlpatterns = [
    re_path(r'^ws/ping/?$', Consumer.as_asgi())
]