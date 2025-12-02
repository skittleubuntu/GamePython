import asyncio
import json

class Client(asyncio.DatagramProtocol):
    def __init__(self, player, server_ip="127.0.0.1", server_port=9999):
        self.player = player
        self.server_addr = (server_ip, server_port)
        self.transport = None
        self.data = None

    async def start(self, loop):
        self.transport, _ = await loop.create_datagram_endpoint(
            lambda: self,
            remote_addr=self.server_addr
        )
        print("Client connected to server", self.server_addr)
        asyncio.create_task(self.receive_loop())

    async def receive_loop(self):
        while True:
            await asyncio.sleep(0.02)

            if hasattr(self, "last_data") and self.last_data:
                self.data = self.last_data
                self.player.eat_data(self.last_data)
                self.last_data = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        try:
            decoded = json.loads(data.decode())
        except:
            decoded = data.decode()
        self.last_data = decoded

    async def send_info(self, jsondata):
        if not self.transport:
            return
        packet = json.dumps(jsondata).encode()
        self.transport.sendto(packet, self.server_addr)


    def get_data(self):
        return self.data
