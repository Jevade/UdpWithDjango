import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udp_socket.settings')

django.setup()

from app.models import Data
from base import UdpServerBase


class RealServer(UdpServerBase):
    def on_data_received(self, address, port, byte_data, str_data):
        # Implement your logic here.
        # This is the part which receives data.
        message = "Received from: {0}, port: {1}. Data: {2}"
        Data.objects.create(message=str_data)
        print(message.format(address, port, str_data))


real_server = RealServer()
