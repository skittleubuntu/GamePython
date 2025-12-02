import asyncio
import json
from player import ServerPlayer

class GameServerProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        super().__init__()
        self.players = {}
        self.outgoing_state = None  # буфер для розсилки

    def connection_made(self, transport):
        self.transport = transport
        print("Server started!")

    def datagram_received(self, data, addr):
        try:
            message = json.loads(data.decode())
        except:
            print("Invalid data from", addr)
            return

        if addr not in self.players:
            pos = message["pos"]
            self.players[addr] = ServerPlayer(pos["x"], pos["y"], pos["angle"])


        self.players[addr].update(message)


        self.prepare_state()

    def prepare_state(self):
        self.outgoing_state = json.dumps({
            "players": {
                str(addr): player.get_data()
                for addr, player in self.players.items()
            }
        }).encode()

    async def broadcast_loop(self):
        while True:
            await asyncio.sleep(0.02)  # 50 FPS оновлення

            if not self.outgoing_state:
                continue

            packet = self.outgoing_state
            for addr in self.players:
                self.transport.sendto(packet, addr)  # async-safe

async def main():
    print("Starting UDP server on 0.0.0.0:9999...")

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: GameServerProtocol(),
        local_addr=("0.0.0.0", 9999)
    )

    # запускаємо асинхронну розсилку
    asyncio.create_task(protocol.broadcast_loop())

    try:
        await asyncio.sleep(3600*24)
    except KeyboardInterrupt:
        transport.close()


if __name__ == "__main__":
    asyncio.run(main())
