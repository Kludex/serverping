import logging
import socket

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from slack import WebClient

from serverpinger.config import settings
from serverpinger.constants import ServerState

app = FastAPI()

server_state = ServerState.UP

client = WebClient(token=settings.SLACK_API_TOKEN)

uvicorn_logger = logging.getLogger("uvicorn")
logger = logging.getLogger(__name__)
logger.handlers = uvicorn_logger.handlers
logger.setLevel(logging.WARNING)


@app.on_event("startup")
@repeat_every(seconds=settings.PING_TIME, raise_exceptions=True)
def startup_event() -> None:
    global server_state
    host, port = settings.HOST, settings.PORT
    channel_id = settings.CHANNEL_ID
    server = settings.SERVER_NAME

    args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    for family, socktype, proto, _, sockaddr in args:
        s = socket.socket(family, socktype, proto)
        try:
            s.connect(sockaddr)
        except socket.error:
            if server_state == ServerState.UP:
                client.chat_postMessage(channel=channel_id, text=f"{server} is down!")
                logger.warning("%s changed from ON to OFF.", server)
                server_state = ServerState.DOWN
        else:
            if server_state == ServerState.DOWN:
                client.chat_postMessage(channel=channel_id, text=f"{server} is up!")
                logger.warning("%s changed from OFF to ON.", server)
                server_state = ServerState.UP
        s.close()
