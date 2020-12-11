from module.protocol.network.messages.SelectedServerDataMessage import SelectedServerDataMessage
from module.protocol.network.types.game_server_informations import GameServerInformations


class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SelectedServerDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8204
        self.servers = {"type": "Vector.<GameServerInformations>", "value": []}

    def deserialize(self):
        super().deserialize()
        server_length = self.buffer_reader.read_ushort()
        for i in range(0, server_length):
            gsi = GameServerInformations()
            gsi.deserialize(self.buffer_reader)
            self.servers.append(gsi)
